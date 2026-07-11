# Galway Finance — Claude Code Wrap-up Skill

Session memory writer. Pair with `/startup`.

- `/startup` **reads** durable context into a Session Brief
- `/wrap-up` **writes** this session's outcomes back to memory

Without wrap-up, the next startup has nothing new to load.

## What it does

1. Reviews the current session (conversation + files changed)
2. Extracts decisions, insights, outcomes, open loops, artifacts
3. Writes to Supabase (preferred) and/or local `memory/` files
4. Optionally stages a git commit note for GitHub backup
5. Returns a short Wrap-up Receipt confirming what was saved

## Install (project-level)

```bash
mkdir -p .claude/skills
cp -R skills/wrap-up .claude/skills/wrap-up
```

## Install (personal — all projects)

```bash
mkdir -p ~/.claude/skills
cp -R skills/wrap-up ~/.claude/skills/wrap-up
```

## CLAUDE.md rule

```markdown
## Session end
Before ending a productive session, run `/wrap-up`.
If scope is clear, pass it: `/wrap-up marketing` or `/wrap-up client:smith`.
Do not skip wrap-up when decisions, deliverables, or open loops were created.
```

## Supabase

Uses the same schema as the startup skill:
`skills/wrap-up/references/supabase-schema.sql`
(identical to startup schema — run once)

Env vars:

```bash
export SUPABASE_URL="https://YOUR_PROJECT.supabase.co"
export SUPABASE_ANON_KEY="YOUR_KEY"
export CLAUDE_MEMORY_PROJECT="galway-finance"
```

## How to use

```text
/wrap-up
/wrap-up marketing
/wrap-up client:smith
/wrap-up dry-run
```

`dry-run` previews what would be saved without writing.

## Package contents

```text
skills/wrap-up/
  SKILL.md
  references/
    supabase-schema.sql
    wrapup-receipt-template.md
  scripts/
    save_context.py
```
