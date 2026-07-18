# Open loops — galway-finance

*Updated 2026-07-18 (Meta health sweep + FB organic post session)*

## Meta ads
1. **Cold duplicate special ad category** — campaign `META_Leads_Broad-Perth_Serviceability-LP_2026-07 – Copy` (120251478141370248) is missing `special_ad_categories` (needs `FINANCIAL_PRODUCTS_SERVICES`); can't be added via API post-creation, must be set in Ads Manager. Owner: Callum.
2. **Cold duplicate Instant Form setup** — `optimization_goal` is still `OFFSITE_CONVERSIONS`, not `LEAD_GENERATION`; the objective change to true on-Facebook Instant Form leads is incomplete. Owner: Callum (doing this himself).
3. **Watch cold duplicate CTR** — currently 0.46% vs the original's 4.35% baseline; geo (Alkimos, 50km) was a deliberate northern-suburbs choice, not a bug — watch whether it recovers over the next few days. Owner: agent (weekly report) / Callum.
4. **WCA booked-exclusion audience** — still too small (`delivery_status` 300) to attach to retargeting ad set 120251478599480248; recheck in a few weeks as bookings accumulate. Owner: agent.
5. **Retargeting duplicate performance** — targeting fixed 2026-07-18 (WCA site-visitors + ECA engagers attached, Advantage+ expansion off); monitor delivery/CPL now that targeting is correct. Owner: agent (weekly report).

## Content
6. **Draft week-2 post** — "Construction Loans in WA: How Progress Payments Actually Work", due ~Jul 20, not yet started. Owner: agent.
7. **Post the FB organic update** — Canva creative ("Couple Engaged Over Kitchen Table Work", further edited by Callum) + "$100,000 apart" caption are ready; Callum to publish to Facebook. Owner: Callum.

## Carried forward (unchanged)
8. **generate_lead tagging** — GA4 still blind to completed bookings; add `generate_lead` on booking confirmation via GTM/WordPress. Owner: agent, needs Callum's go-ahead on approach.
9. **Purple Circle sign-off** on `.claude/AU-finance-compliance.md`. Owner: Callum.
10. **Privacy policy check** — confirm galwayfinance.com.au privacy policy covers Meta pixel remarketing (compliance doc §6). Owner: Callum.
11. **Weekly report cron double-fire** — routine has fired more than once per week previously; needs a check of the trigger config in the Claude Code web UI. Owner: Callum.
12. **product-marketing.md gaps** — metrics, verbatim customer language, named competitors; fill as campaigns surface answers.
13. **Optional cleanup** — 4 orphaned unbranded Canva creative objects in the Meta library. Low priority.

## Resolved this session
- ~~Push pending Jul-13 memory commit~~ — pushed to origin (2314154).
- ~~Cold campaign ad set silently paused~~ — root-caused: Callum had duplicated the campaign Jul 15; original archived, duplicate is the live one (see #1–3 above for its remaining issues).
- ~~Retargeting ad set targeting incomplete~~ — fixed live: WCA site-visitors 90d attached, Advantage+ expansion disabled.
- ~~Archive stale campaigns~~ — both original cold and retargeting campaigns archived.
- ~~Publish week-1 post~~ — confirmed already published (was stale in memory since Jul 12).
- ~~FB organic creative + copy~~ — built and finalized (see Content #7 for the remaining "post it" step).
