# Session — 2026-07-24 — galway-finance

## Objective
Run the ad-hoc Meta Ads performance report for Jul 17-23 and check whether prior open issues (RTG delivery outage, zero leads) had resolved.

## Summary
Startup confirmed Supabase and local memory in sync. Ran the meta-report skill read-only (no changes): zero leads for a 9th consecutive day across all campaigns, verified independently by pulling the live Instant Form's actual submission export since Jul 15 (zero records) — confirming the zero-lead reading is real, not an attribution or reporting gap. The RTG retargeting ad set (`120251560809090248`, ads V6/V7) has now been fully dark for 5 consecutive days (Jul 20-24) despite both ads showing `effective_status ACTIVE` — escalated from the 4-day finding logged Jul 23, still unresolved. Two compliance hygiene gaps surfaced during the pull: the live Instant Form ("Short Details-copy", `2234033924078396`) has no `privacy_policy_url` set at all, and special ad category is inconsistently applied across the two live campaigns (Broad-Perth = `HOUSING`, RTG-Perth = unset), neither matching the previously-decided `FINANCIAL_PRODUCTS_SERVICES`. WoW CTR was down and CPC up, but flagged as noisy given the account is mid-restructure.

## Outcomes
- Delivered Meta Ads report (Jul 17-23) to Callum in chat: TL;DR, numbers table, by-campaign breakdown, signals, 3 ranked recommended actions
- Verified zero-lead reading via direct Instant Form leads export, ruling out an attribution/reporting gap
- Confirmed Instant Form privacy_policy_url is empty — concrete evidence for previously-suspected open loop #3

## Decisions
- None — read-only reporting session, no changes made.

## Insights
- Live Instant Form "Short Details-copy" (`2234033924078396`) has an empty `privacy_policy_url` — confirmed directly, not just suspected.
- Zero Meta lead-ad reporting cross-checked against the Instant Form's actual submissions export (since Jul 15) — both show zero. The zero-lead streak is a real demand/delivery problem, not an attribution or webhook gap.
- RTG ad set dark streak escalated to 5 consecutive days with both ads still `ACTIVE` — `ACTIVE` status does not guarantee delivery on this account. A wait-and-recheck approach has failed twice; next step must be an actual Ads Manager diagnostic.

## Open loops
- RTG ad set (`120251560809090248`) dark 5 days — needs an Ads Manager check for a review/policy hold today, top priority.
- Fix Instant Form (`2234033924078396`) missing `privacy_policy_url` — confirmed empty this session.
- Set `special_ad_category` to `FINANCIAL_PRODUCTS_SERVICES` on both live campaigns (currently `HOUSING` / unset) — API cannot set post-creation, must be done in Ads Manager.
- Judge whether V1/V3/V5 creative underperformance (0 clicks each this week vs V2/V4) is a real pattern once more data accumulates.

## Artifacts
- None persisted — report delivered in chat only (ad-hoc pull, not a scheduled run, so no Notion write per skill scope).

## Tools used
- Pipeboard Meta Ads MCP, Supabase MCP, local memory files, meta-report skill
