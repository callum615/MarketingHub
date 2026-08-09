# Session — 2026-08-09 — galway-finance

## Objective
Fix the broken weekly-marketing-report Meta pull, investigate connecting Google Ads to the workflow, and surface current outstanding items.

## Summary
Startup found local memory 2 weeks stale vs Supabase; treated Supabase as authoritative (newest record 2026-08-03). Diagnosed the weekly-marketing-report failure: `meta-report/SKILL.md` still called the decommissioned Pipeboard tool `get_insights`, causing silent Meta-pull failures on the last two scheduled runs (Jul 20-26, Jul 27-Aug 2) despite the native connector being confirmed live since 07-25. Rewrote it to use the native `ads_get_ad_entities` connector, correcting field names live after an initial guess (`spend`/`actions`/`campaign_name`) was rejected by the API — verified field names are `amount_spent`, `name`, `lead`, `onsite_conversion_lead_grouped`, `omni_complete_registration`, `cost_per_lead`. Verified the fix end-to-end against the live account. Also corrected the GA4 section to stop pointing at a nonexistent `run_google_analytics_report` tool, since no GA4 MCP connector exists in this environment at all.

Live testing surfaced a new critical finding: both Meta campaigns (RTG retargeting and Broad-Perth/cold) are now fully PAUSED account-wide — zero delivery possible.

Then explored connecting Google Ads: confirmed no first-party Anthropic connector exists in the claude.ai directory; found AdvisorPPC (community, covers Google Ads+GA4+GTM+Search Console+YouTube in one OAuth grant) and Windsor.ai (verified but broader/read-only, likely paid) as the two viable third-party options. Recommended AdvisorPPC since it would also close the GA4 gap. Callum began connecting it himself but hit issues on his end; parked for now. Session closed with a consolidated outstanding-items list spanning Meta ads, ad creative refresh, content pipeline, and referral network.

## Outcomes
- Fixed `meta-report/SKILL.md` and `weekly-marketing-report/SKILL.md` — corrected stale Pipeboard tool references to the native Meta connector, verified live against the real ad account
- Discovered and flagged: both Meta campaigns now fully PAUSED account-wide (new finding, not previously in memory)
- Identified AdvisorPPC as the recommended Google Ads/GA4 connector; connection attempt started but parked (issues on Callum's end)
- Compiled a consolidated outstanding-items list across all active workstreams

## Decisions
- **Meta pull tool fix**: `meta-report/SKILL.md` now calls the native connector's `ads_get_ad_entities` (verified fields: `amount_spent`, `name`, `lead`, `onsite_conversion_lead_grouped`, `omni_complete_registration`, `cost_per_lead`) instead of the decommissioned Pipeboard `get_insights` tool.
- **Google Ads / GA4 connector choice (open)**: recommended AdvisorPPC over Windsor.ai or a self-hosted MCP server — Google-only, free-sounding, closes both gaps in one grant, but lowest-tier "Community" review status with some write access (writes require `confirm=true`, no deletes/publishing).

## Insights
- The native Meta connector's `ads_get_ad_entities` does NOT support `spend`, `actions`, or `campaign_name` as field names (Pipeboard/legacy Graph API conventions) — use `amount_spent`, `name`, and dedicated conversion fields instead of a generic actions array. Verified live 2026-08-09.
- A campaign/ad set with zero delivery in the queried window returns "Not available" for all metric fields, not zero — expected behavior, not an API error.
- `weekly-marketing-report`/`meta-report` skill files weren't updated when Pipeboard was decommissioned — they kept referencing its tool name, silently breaking 2 consecutive scheduled reports. Lesson: after a connector migration, grep all skill files for the old tool name, don't just confirm the new connector works ad-hoc.
- No GA4/Google Analytics MCP tool is connected in this environment at all (confirmed via tool search). claude.ai has no first-party Google Ads connector either — only third-party community/verified options (AdvisorPPC, Supermetrics, Coupler.io, Windsor.ai).

## Open loops
- **Confirm both Meta campaigns fully PAUSED account-wide is intentional, or reactivate** — RTG `120251478599460248`, Broad-Perth `120251478141370248`. Owner: Callum. NEW, high priority.
- Commit today's skill fixes (`meta-report/SKILL.md`, `weekly-marketing-report/SKILL.md`) to git — currently modified locally, uncommitted. Owner: agent, on Callum's go-ahead.
- Resolve the AdvisorPPC connector OAuth issue on Callum's end, then wire GA4 + Google Ads into `weekly-marketing-report`/`meta-report` and test live. Owner: Callum → agent.
- `weekly-marketing-report` has not yet been run end-to-end since the fix (only the underlying Meta pull was tested, not a full Notion-writing run). Owner: agent, next scheduled Monday run is the real test.
- Carried forward unchanged: disapproved ad copy push (`120251618482150248`), Instant Form UX audit + missing `privacy_policy_url`, `special_ad_category` fix on both campaigns, manual Ads Manager creative swap for 7 ads (V1-V5, RTG V6-V7), drag 7 PNGs into Notion, build 1:1/9:16 ad formats, 2 overdue blog posts, referral network paperwork/contact ranking/prospect list review.

## Artifacts
None new — only skill files edited (`meta-report/SKILL.md`, `weekly-marketing-report/SKILL.md`).

## Tools used
- mcp__claude_ai_Supabase__* (memory read/write)
- mcp__claude_ai_Meta__* (`ads_get_ad_entities`, `ads_get_ad_accounts`)
- ToolSearch
- mcp__claude-in-chrome__* (browsed claude.ai connector directory)
- Edit/Read, Bash
