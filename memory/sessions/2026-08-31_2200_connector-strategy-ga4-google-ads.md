# Session — 2026-08-31 — galway-finance

## Objective
Restore session context, then resolve which paid/analytics connectors to actually pay for or install.

## Summary
Startup-then-advisory session; no marketing execution. Loaded Supabase memory (current to 2026-08-31) alongside this `emerald-range` worktree's local `memory/` files, which stop at 2026-08-17 — a repeat of the known local-drift pattern, with Supabase again authoritative.

Callum asked whether to pay for Pipeboard or use Pipedrive. These are unrelated products (a decommissioned Meta Ads MCP connector vs a sales CRM) and neither is the fix. Verified live via `ads_get_ad_accounts` that the free native Meta connector reaches Galway Finance account `1928354054506891` (ACTIVE, queryable), so no Meta connector purchase is warranted. Also surfaced that Callum's personal USD ad account `145431623` is DISABLED for unusual activity.

Researched the GA4/Google Ads gap and found the 2026-08-09 AdvisorPPC recommendation is now superseded: Google ships official first-party read-only MCP servers for both GA4 and Google Ads (the latter released 2026-04-28). Critical constraint identified — both are **local stdio** servers, so they fix interactive sessions but cannot fix the 6-week scheduled weekly-report blackout.

## Outcomes
- Native Meta connector confirmed live and free — Pipeboard purchase ruled out
- Pipeboard vs Pipedrive category confusion cleared (CRM ≠ ads connector)
- Personal ad account `145431623` found DISABLED (flagged, all ads paused)
- Official GA4 MCP server identified — `pipx run analytics-mcp`, ADC + `analytics.readonly`, no approval gate
- Official Google Ads MCP server identified — read-only, released 2026-04-28, needs developer token w/ Explorer access, Cloud Run deployable
- Established that local stdio MCP servers cannot serve scheduled/cloud sessions
- Confirmed via tool search that no GA4/Google Ads tooling exists in this environment

## Decisions
- **No paid Meta connector.** Native first-party connector verified sufficient; Pipedrive is not a substitute for one. (decided)
- **GA4/Google Ads connector choice v2 — official Google MCP servers**, not AdvisorPPC. Free, Google-published, strictly read-only (matches the standing "agents never modify live campaigns" rule; AdvisorPPC had write access). GA4 first; Google Ads conditional on real spend. (open — awaiting Callum go-ahead)
- The 2026-08-09 AdvisorPPC decision row is marked `needs_review` / superseded in Supabase.

## Insights
- **Local stdio MCP servers cannot be reached by scheduled or cloud sessions.** This is the structural reason the weekly report keeps coming back empty, and it constrains every connector choice — only remote/hosted connectors can serve a scheduled run. Any "just install the MCP server" fix silently works interactively only.
- Google now publishes first-party read-only MCP servers for GA4 and Google Ads. Re-check first-party availability before recommending any community or paid connector — the landscape moved within 3 weeks of the last recommendation.
- Sequence GA4 before Google Ads: GA4 needs only ADC, Google Ads needs a developer token via an MCC application.
- Local memory drift recurred (third recorded instance). Check Supabase `max(created_at)` before trusting any worktree's local `memory/`.
- Vendor questions can conflate unrelated product categories — check what the product actually solves, and whether a free connector already covers it.

## Open loops
- Decide whether to install the official GA4 MCP server (recommended, ~10 min, no approval gate) — awaiting Callum go-ahead
- Confirm whether Galway Finance actually spends on Google Ads before pursuing a developer token; if not, skip it and GA4 alone closes the gap
- Choose a scheduled-report data path: run weekly report locally, deploy to Cloud Run, or accept a hosted vendor
- Contact Meta about the DISABLED personal ad account `145431623` if still wanted
- **Follow up the 3 referral outreach emails sent 2026-08-17** (Ben Carter, Rachael, Charné Humphreys) — 14 days silent, highest-leverage open item
- Send or drop the A&T Financial Advisers (Tim Vander Kraats) Gmail draft
- Backfill local memory with the 2026-08-24 and 2026-08-31 sessions, or accept Supabase as sole source of truth for this worktree

## Artifacts
- None created this session (advisory only)

## Tools used
Supabase MCP (execute_sql) · Meta MCP (ads_get_ad_accounts) · WebSearch · WebFetch · ToolSearch · Bash · startup skill
