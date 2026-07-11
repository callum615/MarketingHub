#!/usr/bin/env python3
"""Load Claude Code startup context from Supabase.

Usage:
  python3 load_context.py --project galway-finance --limit 10
  python3 load_context.py --project galway-finance --client acme --limit 10

Requires:
  SUPABASE_URL
  SUPABASE_ANON_KEY (or SUPABASE_SERVICE_ROLE_KEY)
  pip install supabase
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any


def die(msg: str, code: int = 1) -> None:
    print(json.dumps({"ok": False, "error": msg}, indent=2))
    raise SystemExit(code)


def get_client():
    url = os.environ.get("SUPABASE_URL")
    key = (
        os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
        or os.environ.get("SUPABASE_ANON_KEY")
    )
    if not url or not key:
        die("Missing SUPABASE_URL and SUPABASE_ANON_KEY/SUPABASE_SERVICE_ROLE_KEY")
    try:
        from supabase import create_client
    except ImportError:
        die("supabase package not installed. Run: pip install supabase")
    return create_client(url, key)


def first_project(sb, project_key: str) -> dict[str, Any] | None:
    res = (
        sb.table("projects")
        .select("*")
        .eq("project_key", project_key)
        .limit(1)
        .execute()
    )
    rows = res.data or []
    return rows[0] if rows else None


def first_client(sb, project_id: str, client_key: str) -> dict[str, Any] | None:
    res = (
        sb.table("clients")
        .select("*")
        .eq("project_id", project_id)
        .eq("client_key", client_key)
        .limit(1)
        .execute()
    )
    rows = res.data or []
    return rows[0] if rows else None


def fetch_many(
    sb,
    table: str,
    project_id: str,
    client_id: str | None,
    limit: int,
    order_col: str = "created_at",
    filters: list[tuple[str, str, Any]] | None = None,
):
    q = sb.table(table).select("*").eq("project_id", project_id)
    if client_id:
        # include project-level rows (null client) + matching client rows
        q = q.or_(f"client_id.is.null,client_id.eq.{client_id}")
    if filters:
        for col, op, val in filters:
            if op == "eq":
                q = q.eq(col, val)
            elif op == "in":
                q = q.in_(col, val)
    res = q.order(order_col, desc=True).limit(limit).execute()
    return res.data or []


def main() -> None:
    parser = argparse.ArgumentParser(description="Load startup memory from Supabase")
    parser.add_argument("--project", default=os.environ.get("CLAUDE_MEMORY_PROJECT", "galway-finance"))
    parser.add_argument("--client", default=None)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    sb = get_client()
    project = first_project(sb, args.project)
    if not project:
        die(f"Project not found: {args.project}. Seed projects table first.")

    client = None
    client_id = None
    if args.client:
        client = first_client(sb, project["id"], args.client)
        if not client:
            die(f"Client not found: {args.client}")
        client_id = client["id"]

    payload = {
        "ok": True,
        "project": project,
        "client": client,
        "preferences": fetch_many(
            sb,
            "preferences",
            project["id"],
            client_id,
            args.limit,
            order_col="priority",
            filters=[("active", "eq", True)],
        ),
        "open_decisions": fetch_many(
            sb,
            "decisions",
            project["id"],
            client_id,
            args.limit,
            order_col="updated_at",
            filters=[("status", "in", ["open", "needs_review"])],
        ),
        "active_workstreams": fetch_many(
            sb,
            "workstreams",
            project["id"],
            client_id,
            args.limit,
            order_col="priority",
            filters=[("status", "in", ["active", "blocked"])],
        ),
        "insights": fetch_many(
            sb,
            "insights",
            project["id"],
            client_id,
            min(args.limit, 5),
            order_col="created_at",
        ),
        "artifacts": fetch_many(
            sb,
            "artifacts",
            project["id"],
            client_id,
            min(args.limit, 5),
            order_col="updated_at",
            filters=[("status", "eq", "active")],
        ),
        "session_logs": fetch_many(
            sb,
            "session_logs",
            project["id"],
            client_id,
            args.limit,
            order_col="created_at",
        ),
    }

    print(json.dumps(payload, indent=2, default=str))


if __name__ == "__main__":
    main()
