# Open loops — galway-finance

*Updated 2026-07-27 (referral network prospect list + builder-finance-arm check) — Meta ads section below is only current as of 2026-07-21; this worktree missed 5 sessions through 2026-07-25 (see `memory/sessions/2026-07-26_1013_referral-network-compliance-fix.md` and Supabase `session_logs` for what changed since, or branch `emerald-range` for the local file trail). Treat Supabase as authoritative for Meta ads state until this file is reconciled.*

## In-person referral network (new workstream, started ~2026-07-21/22)
Full 12-task plan tracked live in Notion: "Referral Network Plan — Progress" (under Marketing Hub).
0. **Get the Purple Circle referral agreement paperwork ready/in hand** — commission-split structure confirmed 2026-07-26 (not pure reciprocity); paperwork itself not yet sourced. Owner: Callum.
1. **Review and approve the drafted one-liner + partner one-pager** — https://app.notion.com/p/3a9c844e9c4381119e22f7784ced6826. Owner: Callum.
2. **List and rank existing loose contacts by type/warmth** — overdue since Jul 22; scoped this session (framework: name / type / how-you-know-them / warmth Hot-Warm-Cold) but Callum hasn't supplied names yet. Owner: Callum.
3. **Build target prospect list (5–8 per type, Perth metro)** — research done 2026-07-27, moved to In Progress. 11 candidates (3 accountants, 2 financial planners, 5-6 real estate/building) — see https://app.notion.com/p/3aac844e9c438185b888c315a1afba8c. Callum to review/vet before outreach. Financial-planner category thin (only 2 clean names — 2 others excluded as they double as mortgage brokers/competitors); consider widening geography. Also unverified: Home Group WA finance arrangement (phone check), Professionals Northern Coast (site 403), Blueprint Homes. Owner: Callum (review) / Agent (research done).
4. Re-engage existing loose contacts (reconnect + coffee ask) — due Jul 28. Owner: Callum.
5. Scope a local networking group (BNI/chamber) — due Aug 1. Owner: Callum.
6. Begin warm-intro/cold outreach to new targets — due Aug 4. Owner: Callum.
7. Give-first referrals to new partners — due Aug 11. Owner: Callum.
8. Set recurring touch cadence per active partner — due Aug 18. Owner: Callum.
9. Fold workstream into this file + galway-finance.md going forward; monthly referral review — due Aug 21. Owner: Agent.

## Meta ads (stale — last verified 2026-07-21, see banner above)
0. **RTG Instant Form ad set delivery check** — `120251560809090248` (ads V6/V7) shows 0 impressions ~16hrs post-creation despite ACTIVE status. Check Ads Manager for a review hold/delivery block. **Due Jul 21** (before the Jul 24-26 checkpoint). Owner: Callum/agent.
0b. **Reconcile cold campaign daily_budget** — live API reads $21.00/day on `120251478141370248`, but the 2026-07-19 session logged $20.00/day. Low priority, not yet investigated. Owner: agent.
1. **Special ad category (both campaigns)** — set `FINANCIAL_PRODUCTS_SERVICES` on cold `120251478141370248` AND retargeting `120251478599460248` in Ads Manager (API can't set post-creation). Live-reconfirmed still unset this session. After applying, recheck the new ad sets' targeting — Meta may reset some of it. Owner: Callum.
2. ~~Fix Lead/CompleteRegistration pixel events on the site~~ — **fixed 2026-07-21**. Root cause was never GTM (site has no classic GTM container — tracking is Site Kit's native "Google tag" `GT-WV3W733W` + a directly-embedded Meta pixel, not routed through Tag Manager). The real gap: the `/booking/` page embeds Calendly, and nothing listened for Calendly's `calendly.event_scheduled` postMessage — so no Lead/CompleteRegistration ever fired on a real booking. Added a message listener in the `page-booking` template's Custom HTML block (JavaScript tab) that fires `fbq('track','Lead')` + `gtag('event','generate_lead')` on that event. Verified live: code confirmed present on the page, and a stubbed-function test dispatch fired both calls correctly. **Still open: confirm a real Calendly booking produces the Lead event in Meta Events Manager and shows up in GA4** — the code path is proven, production has not yet been observed end-to-end. Owner: agent/Callum, next real booking.
3. **Instant Form review** — check form `2234033924078396` questions, privacy policy link, completion message; confirm lead notifications (Leads Center/email) reach Callum for fast follow-up calls. Owner: Callum.
4. **Define a target CPL or lead-volume goal** for the Meta campaigns — none exists in memory; strategy decisions keep being made without a number to judge against. Owner: Callum.
5. **Jul 24–26 checkpoint** (consolidated): judge Instant Form CPL with real data; cut cold ad set `120251560593780248` down to top 2–3 performing ads; compare cold vs retargeting CPL; assess whether the Jul 19 $20/day bump is paying off. Both ad sets restarted learning from zero Jul 19 — don't over-read numbers before this. Owner: agent.
6. **Booked-exclusion audience** `120251421422810248` still too small (code 300) — built on CompleteRegistration, can't grow until #2 is fixed. Recheck after pixel fix. Owner: agent.

## Weekly report
7. **Confirm the idempotency guard holds** — watch the Jul 20 scheduled run fires exactly once and behaves correctly.

## Content
8. **Week-2 blog post** — "Construction Loans in WA: How Progress Payments Actually Work", due Jul 20 (today) — now overdue, still not started. Owner: agent. (Note: V3 Construction is the ad-delivery workhorse — post + ad angle reinforce each other.)
9. **FB organic post** — "$100,000 apart" creative + caption ready; Callum to publish. Owner: Callum.

## Skills/docs hygiene
10. **meta-ad-review SKILL.md stale** — still says HOUSING/CREDIT special ad category; settled decision is FINANCIAL_PRODUCTS_SERVICES. One-line fix. Owner: agent, on explicit ask (non-memory file).

## Carried forward (unchanged)
12. **Purple Circle sign-off** on `.claude/AU-finance-compliance.md`. Owner: Callum.
13. **Privacy policy check** — Meta pixel remarketing coverage. Owner: Callum.
14. **product-marketing.md gaps** — metrics, verbatim customer language, named competitors.
15. **Optional cleanup** — 4 orphaned unbranded Canva creative objects in the Meta library. Low priority.
16. **GA4 hygiene from 2026-07-21 audit**: three phantom conversion events (`purchase`, `close_convert_lead`, `qualify_lead`) marked as conversions but have never fired — never implemented, safe to unmark. Also consider marking `calculator_cta_click`/`contact_cta_click` as key events, and adding a custom dimension for loan-type/page-category (currently zero custom dimensions defined). Low priority, hygiene only.

## Resolved this session (Jul 21 — analytics audit + Calendly tracking fix)
- ~~Dead Lead/CompleteRegistration pixel~~ — root-caused (missing Calendly `event_scheduled` listener, not a GTM issue — site has no classic GTM container) and fixed via a message-listener script added to the `page-booking` template. See #2 above for full detail and the still-open production-verification step.
- ~~generate_lead not marked as GA4 conversion~~ — marked as a key event (ONCE_PER_EVENT) via GA4 Admin API, now that it's wired to a real trigger.
- Full GA4 tracking audit completed — findings logged as #16 above (phantom conversions, missing custom dimensions), all low-priority hygiene.

## Resolved this session (Jul 19 late-evening check)
- ~~Verify 7 new ads cleared Meta review~~ — confirmed all 7 ACTIVE/effective_status ACTIVE (cold V1–V5, RTG V6–V7).
- ~~Reduce ads vs increase budget decision~~ — decided both, sequenced: cold budget $15→$20/day now (executed live), ad-count cut deferred to Jul 24–26 checkpoint with real data.
- ~~Kill retargeting to fund cold bump?~~ — decided no; retargeting kept at $5/day (see project log for rationale).
- ~~Local vs national targeting~~ — decided stay local (Alkimos 50km / northern corridor); rationale in project log.

## Resolved this session
- ~~Zero-lead streak root cause~~ — dead website Lead event + optimization/destination mismatch; fixed by converting both campaigns to Instant Form (LEAD_GENERATION/ON_AD).
- ~~V5 compliance FAIL~~ — Meta text_optimizations auto-variants ("best deal", dropped disclosure) killed via clean single-body creative rebuild.
- ~~Cold duplicate Instant Form setup~~ — done properly via new ad set `120251560593780248` (old one archived).
- ~~Retargeting Perth-40km geo~~ — aligned to Alkimos 50km per Callum (warm audiences kept).
- ~~Weak SEE_DETAILS CTA~~ — LEARN_MORE on rebuilt V5/V6/V7 creatives (V1–V4 keep SEE_DETAILS by scope choice).
