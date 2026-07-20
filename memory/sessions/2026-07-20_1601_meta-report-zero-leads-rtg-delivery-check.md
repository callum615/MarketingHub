# Session — 2026-07-20 — galway-finance

## Objective
Load session context (/startup) and run an ad-hoc Meta Ads performance pull to check on the Jul 19 Instant Form rebuild.

## Summary
Startup brief confirmed Supabase and local `memory/` are in sync (both last updated 2026-07-19). Ran the `meta-report` skill ad-hoc (terminal-only, no Notion write, correctly following the standing rule from 2026-07-18) for the last 7 days at campaign/adset/ad level. Found zero real leads across $192.28 spend for the week — the one "lead" action in the data is a stale, delayed-attribution artifact on a paused $0-spend campaign, not a new lead. Drilled into the two new Instant Form ad sets created late Jul 19: the cold one (5 ads, `120251560593780248`) has started delivering (~$25 spend, very low CTR, too small a sample to judge) but the retargeting one (`120251560809090248`, ads V6/V7) shows **zero impressions at all** since creation ~16 hours earlier despite `effective_status: ACTIVE` — a new finding not previously in memory. Also noticed the cold campaign's live API `daily_budget` reads $21.00 (2100 cents), not the $20.00 logged in the 2026-07-19 budget-bump session — a small reconciliation gap, not acted on. Gave Callum a two-tier check-in recommendation: Jul 21 for the RTG delivery question, Jul 24–26 for the already-agreed full performance checkpoint.

## Outcomes
- Session brief delivered (Supabase + local memory confirmed consistent)
- Ad-hoc 7-day Meta report produced in terminal (read-only, no changes made, no Notion write)
- Identified RTG Instant Form ad set delivering zero impressions since creation — flagged for a Jul 21 check
- Recommended check-in cadence to Callum: Jul 21 (RTG delivery) + Jul 24–26 (full checkpoint, unchanged)

## Decisions
None settled this session — read-only reporting only.

## Insights
- RTG Instant Form ad set `120251560809090248` (ads V6/V7) shows 0 impressions ~16hrs post-creation despite ACTIVE status — unusual; needs a quick Ads Manager check for a review hold or delivery block, not just "wait for the Jul 24-26 checkpoint."
- Live API `daily_budget` on the cold campaign (`120251478141370248`) reads $21.00/day, not the $20.00/day recorded in the 2026-07-19 wrap-up. Not investigated further this session — flagged as a small discrepancy to reconcile, not a live problem.

## Open loops
- Check RTG ad set `120251560809090248` delivery status by **Jul 21** — confirm it's not stuck in review/blocked (new, more urgent than the Jul 24-26 checkpoint). Owner: agent/Callum.
- Reconcile cold campaign `daily_budget` figure: live API shows $21.00/day vs $20.00/day logged Jul 19. Low priority. Owner: agent.
- Jul 24-26 full checkpoint (unchanged, carried from prior session): judge Instant Form CPL with real data, cut cold ad set to top 2-3 ads, compare cold vs retargeting CPL, assess $20/21-day bump.
- All open loops from the 2026-07-19 session remain outstanding (special ad category, pixel event fix, Instant Form review, week-2 blog post — due today and still not started as of this session, FB organic post still awaiting Callum to publish).

## Artifacts
None created this session (terminal report only, not saved to a file or Notion).

## Tools used
Supabase (local `load_context.py` loader), Meta Ads MCP (`get_insights`, `get_campaigns`, `get_ads`), local `memory/` files, `git log`/`git status`.
