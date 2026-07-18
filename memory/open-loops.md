# Open loops — galway-finance

*Updated 2026-07-18 (weekly-report fix + ad-hoc Meta check session)*

## Meta ads
1. **Zero-lead streak (critical)** — no lead or website conversion of any kind since Jul 13 (5 days, ~$119.66 spent) across the cold + retargeting duplicate campaigns. Owner: Callum.
2. **Verify Events Manager / pixel firing** — the serviceability landing page has 11 views but zero downstream conversion events on the cold duplicate; check whether the conversion pixel event is configured/firing at all — this is the more likely zero-lead cause, more so than the special_ad_category gap. Owner: Callum.
3. **Cold duplicate special ad category** — campaign `META_Leads_Broad-Perth_Serviceability-LP_2026-07 – Copy` (120251478141370248) is missing `special_ad_categories` (needs `FINANCIAL_PRODUCTS_SERVICES`); can't be added via API post-creation, must be set in Ads Manager. This is a targeting/compliance risk, not the tracking fix. Owner: Callum.
4. **Cold duplicate Instant Form setup** — `optimization_goal` is still `OFFSITE_CONVERSIONS`, not `LEAD_GENERATION`; the objective change to true on-Facebook Instant Form leads is incomplete. Owner: Callum (doing this himself).
5. **Watch cold duplicate CTR** — recovering (0.43% → 0.57% → 0.97% Jul 16–18) but still below the original's 4.35% baseline; geo (Alkimos, 50km) was a deliberate northern-suburbs choice, not a bug. Owner: Callum.
6. **WCA booked-exclusion audience** — still too small (`delivery_status` 300) to attach to retargeting ad set 120251478599480248; recheck in a few weeks as bookings accumulate. Owner: agent.

## Weekly report
7. **Confirm the idempotency guard holds** — `.claude/skills/weekly-marketing-report/SKILL.md` now checks Notion for an existing week's page before touching Meta/GA4 (added 2026-07-18); watch Jul 20 to confirm it fires exactly once and behaves correctly.

## Content
8. **Draft week-2 post** — "Construction Loans in WA: How Progress Payments Actually Work", due ~Jul 20, not yet started. Owner: agent.
9. **Post the FB organic update** — Canva creative ("Couple Engaged Over Kitchen Table Work", further edited by Callum) + "$100,000 apart" caption are ready; Callum to publish to Facebook. Owner: Callum.

## Carried forward (unchanged)
10. **generate_lead tagging** — GA4 still blind to completed bookings; add `generate_lead` on booking confirmation via GTM/WordPress. Owner: agent, needs Callum's go-ahead on approach.
11. **Purple Circle sign-off** on `.claude/AU-finance-compliance.md`. Owner: Callum.
12. **Privacy policy check** — confirm galwayfinance.com.au privacy policy covers Meta pixel remarketing (compliance doc §6). Owner: Callum.
13. **product-marketing.md gaps** — metrics, verbatim customer language, named competitors; fill as campaigns surface answers.
14. **Optional cleanup** — 4 orphaned unbranded Canva creative objects in the Meta library. Low priority.

## Resolved this session
- ~~Weekly report "double-fire"~~ — root-caused as Callum's own manual RemoteTrigger test runs (not a scheduler bug); the trigger's cron config was already correct. Fixed by adding an idempotency guard to the skill and agreeing to use `meta-report` ad-hoc for on-demand figures instead of manually firing the trigger.
- ~~Diagnose zero-lead cause~~ — clarified special_ad_category (targeting/compliance) vs optimization_goal/Instant Form (tracking) as distinct mechanisms; pointed at Events Manager/pixel firing as the next concrete check (see Meta ads #2).
