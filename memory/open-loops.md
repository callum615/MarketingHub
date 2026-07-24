# Open loops — galway-finance

*Updated 2026-07-24 (meta-report)*

## Meta ads
-1. **RTG retargeting ad set fully dark, 5 consecutive days** — `120251560809090248` shows zero impressions/spend Jul 20-24 (escalated again from the 4-day note on Jul 23; both ads V6/V7 still show `effective_status: ACTIVE`). Two wait-and-recheck cycles have now failed — needs an actual Ads Manager diagnostic (review hold / delivery restriction check) today. Owner: Callum/agent. **Still the top priority.**
-0. **Instant Form missing privacy policy link** — live form "Short Details-copy" (`2234033924078396`) has an empty `privacy_policy_url`, confirmed directly via API on 2026-07-24 (previously only suspected under open loop #3 below). Quick compliance fix. Owner: Callum.
0b. **Reconcile cold campaign daily_budget** — was $21.00/day (Jul 20), now confirmed intentionally cut to $15.00/day (changed 2026-07-22) to fund the new broader-Australia test ad set. Resolved as intentional, no longer a discrepancy to chase.
1. **Special ad category (both campaigns)** — set `FINANCIAL_PRODUCTS_SERVICES` on cold `120251478141370248` (currently `HOUSING`, a stale value) AND retargeting `120251478599460248` (currently unset) in Ads Manager (API can't set post-creation). Confirmed live via API on 2026-07-24. After applying, recheck the new ad sets' targeting — Meta may reset some of it. Owner: Callum.
1b. **Monitor new "Test - Broad Australia — Instant Form leads" ad set** (`120251618482160248`) — confirmed intentional broader-market test (Callum's lifestyle/relocation interest), not drift. Track its performance alongside the local ad set. Owner: agent.
2. ~~Fix Lead/CompleteRegistration pixel events on the site~~ — **fixed 2026-07-21**. Root cause was never GTM (site has no classic GTM container — tracking is Site Kit's native "Google tag" `GT-WV3W733W` + a directly-embedded Meta pixel, not routed through Tag Manager). The real gap: the `/booking/` page embeds Calendly, and nothing listened for Calendly's `calendly.event_scheduled` postMessage — so no Lead/CompleteRegistration ever fired on a real booking. Added a message listener in the `page-booking` template's Custom HTML block (JavaScript tab) that fires `fbq('track','Lead')` + `gtag('event','generate_lead')` on that event. Verified live: code confirmed present on the page, and a stubbed-function test dispatch fired both calls correctly. **Still open: confirm a real Calendly booking produces the Lead event in Meta Events Manager and shows up in GA4** — the code path is proven, production has not yet been observed end-to-end. Owner: agent/Callum, next real booking.
3. **Instant Form review** — privacy policy link confirmed missing (see -0 above, 2026-07-24). Still need to check form `2234033924078396` questions and completion message; confirm lead notifications (Leads Center/email) reach Callum for fast follow-up calls. Owner: Callum.
4. **Define a target CPL or lead-volume goal** for the Meta campaigns — none exists in memory; strategy decisions keep being made without a number to judge against. Owner: Callum.
5. **Jul 24–26 checkpoint** (consolidated): ~~cut cold ad set `120251560593780248` down to top 2-3 ads~~ — **done 2026-07-23**, V3/V5 paused, V1/V2/V4 kept live. Remaining: judge Instant Form CPL with real data once RTG delivery is restored; compare cold vs retargeting CPL; assess whether the $15/day reallocation (post broader-market pivot) is paying off. Owner: agent.
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

## Resolved this session (Jul 23 — meta-report + creative cut)
- ~~Broader-Australia targeting ad set + cold budget drop to $15/day: unlogged drift or deliberate?~~ — confirmed deliberate; Callum is intentionally broadening market scope ahead of a possible relocation.
- ~~Cold ad set creative cut (Jul 24-26 checkpoint)~~ — done early: V3 and V5 paused, V1/V2/V4 kept live.

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
