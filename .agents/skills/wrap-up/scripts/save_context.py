#!/usr/bin/env python3
"""Save Claude Code wrap-up memory to Supabase.

Usage:
  python3 save_context.py --project galway-finance --payload /tmp/wrapup_payload.json
  python3 save_context.py --project galway-finance --client acme --payload ./payload.json

Requires:
  SUPABASE_URL
  SUPABASE_ANON_KEY (or SUPABASE_SERVICE_ROLE_KEY)
  pip install supabase

Payload JSON shape:
{
  "objective": "...",
  "summary": "...",
  "outcomes": ["..."],
  "open_loops": ["..."],
  "tools_used": ["..."],
  "raw_notes": "optional",
  "decisions": [{"title": "...", "decision": "...", "rationale": "...", "status": "decided|open|needs_review"}],
  "insights": [{"insight": "...", "importance": 3, "tags": ["marketing"]}],
  "artifacts": [{"artifact_type": "report", "title": "...", "path_or_url": "...", "summary": "...", "status": "active"}],
  "preferences": [{"key": "tone", "value": "direct", "priority": 100}],
  "workstreams": [{"title": "...", "goal": "...", "status": "active", "next_action": "...", "priority": 100}]
}
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
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


def ensure_project(sb, project_key: str, display_name: str | None = None) -> dict[str, Any]:
    res = (
        sb.table("projects")
        .select("*")
        .eq("project_key", project_key)
        .limit(1)
        .execute()
    )
    rows = res.data or []
    if rows:
        return rows[0]
    insert = {
        "project_key": project_key,
        "display_name": display_name or project_key.replace("-", " ").title(),
        "domain": "general",
    }
    created = sb.table("projects").insert(insert).execute()
    if not created.data:
        die(f"Failed to create project: {project_key}")
    return created.data[0]


def ensure_client(sb, project_id: str, client_key: str, display_name: str | None = None) -> dict[str, Any]:
    res = (
        sb.table("clients")
        .select("*")
        .eq("project_id", project_id)
        .eq("client_key", client_key)
        .limit(1)
        .execute()
    )
    rows = res.data or []
    if rows:
        return rows[0]
    insert = {
        "project_id": project_id,
        "client_key": client_key,
        "display_name": display_name or client_key.replace("-", " ").title(),
        "status": "active",
    }
    created = sb.table("clients").insert(insert).execute()
    if not created.data:
        die(f"Failed to create client: {client_key}")
    return created.data[0]


def main() -> None:
    parser = argparse.ArgumentParser(description="Save wrap-up memory to Supabase")
    parser.add_argument("--project", default=os.environ.get("CLAUDE_MEMORY_PROJECT", "galway-finance"))
    parser.add_argument("--client", default=None)
    parser.add_argument("--payload", required=True, help="Path to wrap-up payload JSON")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    payload_path = Path(args.payload)
    if not payload_path.exists():
        die(f"Payload not found: {payload_path}")

    try:
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        die(f"Invalid payload JSON: {exc}")

    if args.dry_run:
        print(json.dumps({"ok": True, "dry_run": True, "payload": payload}, indent=2))
        return

    sb = get_client()
    project = ensure_project(sb, args.project)
    client = None
    client_id = None
    if args.client:
        client = ensure_client(sb, project["id"], args.client)
        client_id = client["id"]

    result: dict[str, Any] = {
        "ok": True,
        "project": project,
        "client": client,
        "inserted": {
            "session_logs": 0,
            "decisions": 0,
            "insights": 0,
            "artifacts": 0,
            "preferences": 0,
            "workstreams": 0,
        },
        "ids": {},
    }

    session_row = {
        "project_id": project["id"],
        "client_id": client_id,
        "objective": payload.get("objective"),
        "summary": payload.get("summary") or "Session wrap-up",
        "outcomes": payload.get("outcomes") or [],
        "open_loops": payload.get("open_loops") or [],
        "tools_used": payload.get("tools_used") or [],
        "raw_notes": payload.get("raw_notes"),
    }
    session_res = sb.table("session_logs").insert(session_row).execute()
    if session_res.data:
        result["inserted"]["session_logs"] = 1
        result["ids"]["session_log"] = session_res.data[0].get("id")

    for item in payload.get("decisions") or []:
        row = {
            "project_id": project["id"],
            "client_id": client_id,
            "title": item.get("title") or "Decision",
            "decision": item.get("decision") or "",
            "rationale": item.get("rationale"),
            "status": item.get("status") or "decided",
        }
        if not row["decision"]:
            continue
        res = sb.table("decisions").insert(row).execute()
        if res.data:
            result["inserted"]["decisions"] += 1

    for item in payload.get("insights") or []:
        insight = item.get("insight") if isinstance(item, dict) else str(item)
        if not insight:
            continue
        row = {
            "project_id": project["id"],
            "client_id": client_id,
            "insight": insight,
            "importance": (item.get("importance") if isinstance(item, dict) else 3) or 3,
            "tags": (item.get("tags") if isinstance(item, dict) else []) or [],
        }
        res = sb.table("insights").insert(row).execute()
        if res.data:
            result["inserted"]["insights"] += 1

    for item in payload.get("artifacts") or []:
        if not item.get("title"):
            continue
        row = {
            "project_id": project["id"],
            "client_id": client_id,
            "artifact_type": item.get("artifact_type") or "other",
            "title": item["title"],
            "path_or_url": item.get("path_or_url"),
            "status": item.get("status") or "active",
            "summary": item.get("summary"),
        }
        res = sb.table("artifacts").insert(row).execute()
        if res.data:
            result["inserted"]["artifacts"] += 1

    for item in payload.get("preferences") or []:
        if not item.get("key") or not item.get("value"):
            continue
        row = {
            "project_id": project["id"],
            "client_id": client_id,
            "key": item["key"],
            "value": item["value"],
            "priority": item.get("priority") or 100,
            "active": True,
        }
        res = sb.table("preferences").insert(row).execute()
        if res.data:
            result["inserted"]["preferences"] += 1

    for item in payload.get("workstreams") or []:
        if not item.get("title"):
            continue
        row = {
            "project_id": project["id"],
            "client_id": client_id,
            "title": item["title"],
            "goal": item.get("goal"),
            "status": item.get("status") or "active",
            "next_action": item.get("next_action"),
            "priority": item.get("priority") or 100,
        }
        res = sb.table("workstreams").insert(row).execute()
        if res.data:
            result["inserted"]["workstreams"] += 1

    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
