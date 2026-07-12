---
name: wrap-up
description: Save durable session memory to Supabase and local files at the end of a Claude Code session. Use when the user says wrap-up, wrap up, save memory, end session, close session, or finish up and wants outcomes, decisions, insights, and open loops persisted for the next /startup.
when_to_use: End of productive sessions; user says /wrap-up, save memory, end session, or close out work.
argument-hint: "[project-or-client|dry-run]"
disable-model-invocation: true
---

# Wrap-up — Session Memory Writer

You are closing a Claude Code session for **Callum Duffy / Galway Finance**.

Goal: persist high-signal memory so the next `/startup` compounds. Save decisions, outcomes, insights, artifacts, and open loops. Do **not** dump the full transcript.

## Arguments

- `$ARGUMENTS` may include:
  - project/client/domain hint (`marketing`, `compliance`, `client:smith`)
  - `dry-run` to preview writes without saving
- If empty, infer scope from cwd, git remote, and session content

## Procedure (follow in order)

### 1) Identify scope

Determine:

- `project_key` (default `galway-finance` or env `CLAUDE_MEMORY_PROJECT`)
- `client_key` if mentioned or clear from work
- `domain`: `broker-ops` | `marketing` | `compliance` | `product` | `general`
- `dry_run`: true if args contain `dry-run`

State scope in one line before extracting memory.

### 2) Extract memory from this session only

From the conversation and files touched this session, extract:

| Field | Rules |
|---|---|
| `objective` | What this session set out to do (1 sentence) |
| `summary` | What happened (3–6 sentences max) |
| `outcomes` | Concrete deliverables / results (array of short strings) |
| `decisions` | Settled choices + rationale (only if actually decided) |
| `insights` | Preferences, standards, lessons worth reusing |
| `open_loops` | Unfinished next actions (actionable, not vague) |
| `artifacts` | Files/URLs/pages/campaigns created or updated |
| `tools_used` | MCPs/CLIs/skills used |
| `preferences` | Standing rules the user stated for future sessions |
| `workstream_updates` | Status/next_action changes for active work |

Rules:

- Prefer precision over volume
- Do not invent outcomes that did not happen
- Do not store secrets, API keys, tokens, passwords, or raw credentials
- Do not store full transcripts
- If nothing durable happened, say so and offer a minimal log or skip

### 3) Confirm with user when ambiguous

If the session is long or messy and extraction is uncertain, show a short draft of:

- outcomes
- decisions
- open loops

and ask for a yes/edit before writing. If the session is clear, write without extra confirmation unless `dry-run`.

### 4) Write memory (unless dry-run)

Try writers in order. Report what succeeded.

**A. Supabase (preferred)**

If Supabase MCP/CLI or credentials exist, upsert/insert:

1. Ensure `projects` row exists for `project_key`
2. Ensure `clients` row if `client_key` present
3. Insert `session_logs` with summary, outcomes, open_loops, tools_used
4. Insert new `decisions` (status `decided` if settled, else `open`)
5. Insert `insights` (importance 1–5; default 3)
6. Insert/update `artifacts` for tangible outputs
7. Upsert `preferences` when user stated standing rules
8. Update `workstreams` next_action/status when relevant; create if a new initiative clearly started

Use schema in `references/supabase-schema.sql`.

If Python saver is available:

```bash
python3 .claude/skills/wrap-up/scripts/save_context.py \
  --project "$PROJECT" \
  --client "$CLIENT" \
  --payload /tmp/wrapup_payload.json
```

(or `~/.claude/skills/wrap-up/scripts/save_context.py`)

Build `/tmp/wrapup_payload.json` from the extracted fields first.

**B. Local project files (always do as fallback or dual-write)**

Create dirs if needed:

```text
memory/
  sessions/
  projects/
  clients/
```

Write/update:

1. `memory/sessions/YYYY-MM-DD_HHMM_<slug>.md` — full wrap-up note for this session
2. `memory/open-loops.md` — replace/merge open loops for this project/client
3. `memory/projects/<project_key>.md` — append latest summary + key decisions
4. `memory/clients/<client_key>.md` — if client scoped
5. `memory/PREFERENCES.md` — append only new standing preferences

Session note format:

```markdown
# Session — <date> — <project_key>

## Objective
...

## Summary
...

## Outcomes
- ...

## Decisions
- ...

## Insights
- ...

## Open loops
- ...

## Artifacts
- ...

## Tools used
- ...
```

**C. Git backup (commit + push memory files)**

If git repo exists and memory files changed (skip entirely on `dry-run`):

1. Stage **only** memory paths (`memory/`) — never bundle unrelated working-tree changes
2. Commit with message: `memory: wrap-up <project_key> <date>`
3. `git push` to origin
4. If other non-memory changes from this session are uncommitted, mention them in the receipt but leave them alone unless the user asks

If commit or push fails (auth, network, conflicts), report the error in the receipt and continue — local + Supabase writes still count as saved.

### 5) Output format (always)

Return a **Wrap-up Receipt** using `references/wrapup-receipt-template.md`:

1. **Scope**
2. **Saved** — counts by type (sessions, decisions, insights, artifacts, preferences, workstreams)
3. **Open loops carried forward**
4. **Write targets** — `supabase | local | both | none` + paths/IDs if known
5. **Git** — pushed commit hash, or why commit/push was skipped/failed
6. **Dry run?** — yes/no
7. **Next session hint** — one line the next `/startup` should prioritise

Keep the receipt short.

### 6) Operating defaults

- Business: Galway Finance, Callum Duffy, Australia/Perth
- Purple Circle compliance context when relevant
- Notion = human docs/CRM; Supabase = agent memory
- Quality bar: only store what improves future execution

## Failure modes

| Situation | Response |
|---|---|
| No Supabase credentials | Local write only; report gap |
| Supabase write fails | Keep local write; show error summary |
| Git commit/push fails | Report in receipt; memory writes still count as saved |
| Nothing durable to save | Say so; optional minimal session log |
| dry-run | Preview payload only; no writes |
| Secrets in draft | Redact before any write |
| User declines save | Abort writes; keep draft in chat only |

## Quality bar for what to store

Store if it helps future sessions:
- decisions that should stay settled
- preferences about quality, voice, process
- artifacts worth reusing
- open loops with clear owners/actions

Do **not** store:
- chit-chat
- failed dead ends with no lesson
- raw dumps of code or data unless they are the artifact reference
