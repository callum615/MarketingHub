# Galway Finance — Claude Code Startup Skill

Session memory loader aligned to the WebProfits Claude Code stack:
**Terminal + Claude Code → Supabase memory → GitHub backup → skills**.

This skill runs at the start of a session, pulls durable context from Supabase
(and local project files), and produces a short **Session Brief** so Claude does
not relearn your business every time.

## What it does

1. Identifies the active project/client from the current folder and optional args
2. Loads recent session memory, open decisions, preferences, and active work
3. Summarises into a compact brief (not a dump of every past note)
4. States assumptions and gaps if Supabase is not connected yet

## Install (project-level)

From your project root (recommended: `galway-finance/`):

```bash
mkdir -p .claude/skills
cp -R skills/startup .claude/skills/startup
```

Or copy the whole `skills/startup` folder from this package into:

```text
.claude/skills/startup/
```

## Install (personal — all projects)

```bash
mkdir -p ~/.claude/skills
cp -R skills/startup ~/.claude/skills/startup
```

## Auto-run on session start

Add this to your project `CLAUDE.md`:

```markdown
## Session start
At the beginning of every session, run `/startup` before other work.
If the user names a client or project, pass it: `/startup locksmith` or `/startup marketing`.
```

Optional: configure Claude Code so startup is your default first command.

## Supabase setup (required for compounding memory)

1. Create a Supabase project
2. Run `skills/startup/references/supabase-schema.sql` in the SQL editor
3. Set env vars (shell profile or project `.env` loaded by your tooling):

```bash
export SUPABASE_URL="https://YOUR_PROJECT.supabase.co"
export SUPABASE_ANON_KEY="YOUR_ANON_OR_SERVICE_KEY"
# optional default project key used when cwd is ambiguous
export CLAUDE_MEMORY_PROJECT="galway-finance"
```

4. Prefer connecting Supabase via MCP/CLI inside Terminal so Claude can query
   directly. The skill supports:
   - Supabase MCP / CLI if available
   - `scripts/load_context.py` if `supabase` Python client + env vars are set
   - Graceful local fallback if neither is available

## How to use

```text
/startup
/startup marketing
/startup galway-finance
/startup client:acme-referrer
```

Then do real work. At session end, run your wrap-up skill (pair skill) so the
next `/startup` is smarter.

## Package contents

```text
skills/startup/
  SKILL.md
  references/
    supabase-schema.sql
    context-brief-template.md
  scripts/
    load_context.py
```

## Recommended first week

1. Install skill + schema
2. Run `/startup` every session even if memory is empty
3. After work, save decisions/outcomes via wrap-up
4. Re-run `/startup` next day and confirm recall improves
