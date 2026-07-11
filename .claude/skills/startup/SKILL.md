---
name: startup
description: Load durable session memory from Supabase/GitHub/local project files and produce a Session Brief. Use at the start of every Claude Code session, when resuming work, or when the user says startup, load memory, load context, or continue where we left off.
when_to_use: Session start; resume work; user says /startup, load memory, load context, or continue previous work.
argument-hint: "[project-or-client]"
---

# Startup — Session Memory Loader

You are booting a Claude Code session for **Callum Duffy / Galway Finance** (Australian mortgage broker, Purple Circle, marketing + ops automation).

Goal: restore high-signal context fast. Do **not** dump raw history. Produce a tight **Session Brief**, then wait for direction unless the user already gave a task.

## Arguments

- `$ARGUMENTS` may contain a project, client, or domain hint (e.g. `marketing`, `compliance`, `client:smith`).
- If empty, infer from current working directory, git remote, and recent files.

## Procedure (follow in order)

### 1) Identify active scope

Determine:

- `project_key` (default `galway-finance` or env `CLAUDE_MEMORY_PROJECT`)
- `client_key` if mentioned or obvious from folder path
- `domain` one of: `broker-ops`, `marketing`, `compliance`, `product`, `general`

State the chosen scope in one line before loading data.

### 2) Load memory sources (best available first)

Try sources in this order. Skip quietly if unavailable. Never invent memory.

**A. Supabase (preferred)**

If Supabase MCP/CLI or credentials exist, query recent memory for the active scope:

1. Last 10 `session_logs` for this project/client
2. Open `decisions` (`status = open` or `needs_review`)
3. Active `workstreams` (`status in (active, blocked)`)
4. Top preferences / standing instructions for this project
5. Last 5 high-importance `insights`
6. Any `artifacts` marked `active` (reports, pages, campaigns, skills)

Use schema in `references/supabase-schema.sql`.

If Python loader is available:

```bash
python3 .claude/skills/startup/scripts/load_context.py --project "$PROJECT" --client "$CLIENT" --limit 10
```

(or the personal path `~/.claude/skills/startup/scripts/load_context.py`)

**B. Local project files**

Read if present (do not create yet unless user asks):

- `CLAUDE.md`, `.claude/CLAUDE.md`
- `memory/PROFILE.md`, `memory/PREFERENCES.md`
- `memory/projects/<project_key>.md`
- `memory/clients/<client_key>.md`
- `memory/open-loops.md`
- recent files in `memory/sessions/` (latest 3 only)

**C. Git / workspace signals**

- `git status -sb` and last 5 commits (titles only)
- outstanding TODO/FIXME in recently touched files only if clearly relevant

### 3) Synthesise — do not regurgitate

Compress loaded material into the Session Brief template in
`references/context-brief-template.md`.

Rules:

- Prefer decisions, constraints, active work, and next actions over narrative
- Keep total brief under ~400 words unless user asks for deep recall
- Mark uncertainty explicitly (`Unknown`, `Not in memory`)
- If memory is empty, say so and give a 4-step bootstrap checklist
- Never claim Supabase was queried if it was not

### 4) Output format (always)

Return exactly these sections:

1. **Scope** — project / client / domain
2. **Session Brief** — filled template
3. **Recommended next actions** — 3 bullets max, ordered by leverage
4. **Memory status** — `supabase | local | none` + recency of newest record
5. **Ready** — one line: what you need from the user to start execution

### 5) Operating defaults for this business

Apply unless memory overrides:

- Business: Galway Finance (mortgage broking), Callum Duffy, Australia/Perth
- Aggregator/compliance context: Purple Circle standards where relevant
- Quality bar: shippable work only; no generic filler outputs
- Stack intent: Terminal + Claude Code, Supabase memory, GitHub backup, MCP connectors
- Prefer Notion for human-facing docs/CRM; Supabase for agent session memory

### 6) After the brief

- If user already stated a task in this message, proceed immediately after the brief
- Otherwise stop after the brief and wait
- Do not start large builds during startup unless asked

## Failure modes

| Situation | Response |
|---|---|
| No Supabase credentials | Use local memory; report gap; continue |
| Supabase query fails | Show error summary; fall back to local |
| Empty memory | Bootstrap checklist; still provide scope + defaults |
| Conflicting notes | Prefer newest dated decision; flag conflict |
| Secrets in memory rows | Never echo API keys/tokens; redaction only |

## Bootstrap checklist (only if memory empty)

1. Confirm Supabase schema applied
2. Set `SUPABASE_URL` + key env vars / MCP
3. Create `memory/PROFILE.md` with business facts
4. After first real work session, run wrap-up to write first `session_logs` row
