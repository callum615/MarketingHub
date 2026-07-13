# Open loops — galway-finance

*Updated 2026-07-13 night (Meta retargeting build session)*

## Retargeting (new this session)
1. **Activate retargeting campaign** — `META_Leads_RTG-Perth_Serviceability-LP_2026-07` (120251420896860248) is fully built and PAUSED; flip ACTIVE once the 2 ads clear Meta review. Owner: Callum (or tell agent).
2. **API-verify retargeting ad set targeting** — Callum manually attached WCA site-visitors + booked-exclusion in Ads Manager after Pipeboard's weekly limit blocked the call; verify via `get_adset_details 120251421081140248` when the limit resets. Owner: agent.
3. **Live campaign special ad category** — API reads `special_ad_categories: []` on the live serviceability campaign while correctly echoing the new campaign's FINANCIAL_PRODUCTS_SERVICES; likely genuinely missing → policy risk. Check in Ads Manager; agent can fix via API with go-ahead. Owner: Callum.
4. **Privacy policy check** — confirm galwayfinance.com.au privacy policy covers Meta pixel remarketing (compliance doc §6). Owner: Callum.
5. **Watch retargeting frequency** once live — small warm pool at A$5/day; refresh creative if frequency >4/week. Owner: agent (weekly report).

## Carried forward
6. **Publish week-1 post** — WP draft 50 ("How Much Can I Borrow?"), staged & compliance-checked. Owner: Callum. 2 min.
7. **Confirm V1 hero ad cleared Meta review** — cold campaign; was PENDING_REVIEW at Jul 12 close; not checked since (Pipeboard limit). Owner: agent.
8. **Cold campaign Tue check (Jul 14)** — day-1 was strong (CTR 3.8%, CPC A$1.02, 10 link clicks); prior flight fatigued within 3 days, keep watching CPL vs ~A$5.60 baseline. Note: report cold and retargeting CPL separately.
9. **generate_lead tagging** — GA4 still blind to completed bookings; add generate_lead on booking confirmation via GTM/WordPress. Owner: agent, needs Callum's go-ahead on approach.
10. **Purple Circle sign-off** on `.claude/AU-finance-compliance.md`. Owner: Callum.
11. **Duplicate report check** — two "Scheduled weekly marketing report" session logs on Jul 13; check Marketing Hub for a stray report page.
12. **product-marketing.md gaps** — metrics, verbatim customer language, named competitors; fill as campaigns surface answers.
13. **Optional cleanup** — 4 orphaned unbranded Canva creative objects in the Meta library. Low priority.

## Resolved this session
- ~~Custom Audience ToS~~ — accepted at both scopes + web_custom_audience_tos; audiences created.
- ~~Commit wrap-up skill change~~ — committed as 0533824 before this session.
- ~~Monitor new campaign Mon (Jul 13)~~ — done: strong day-1; continues as #8.
