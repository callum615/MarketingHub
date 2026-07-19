# Open loops — galway-finance

*Updated 2026-07-19 (late evening — Meta ad review + budget bump session)*

## Meta ads
1. **Special ad category (both campaigns)** — set `FINANCIAL_PRODUCTS_SERVICES` on cold `120251478141370248` AND retargeting `120251478599460248` in Ads Manager (API can't set post-creation). Live-reconfirmed still unset this session. After applying, recheck the new ad sets' targeting — Meta may reset some of it. Owner: Callum.
2. **Fix Lead/CompleteRegistration pixel events** on the site — no longer blocks lead optimization (both campaigns now Instant Form), but blocks: booked-exclusion audience growth, retargeting hygiene, GA4 lead visibility. Check Events Manager Test Events on `/new-home-borrowing-power/` + GTM trigger URL scope (event fired under old campaign, 0 times since Jul 15 relaunch). Owner: Callum.
3. **Instant Form review** — check form `2234033924078396` questions, privacy policy link, completion message; confirm lead notifications (Leads Center/email) reach Callum for fast follow-up calls. Owner: Callum.
4. **Define a target CPL or lead-volume goal** for the Meta campaigns — none exists in memory; strategy decisions keep being made without a number to judge against. Owner: Callum.
5. **Jul 24–26 checkpoint** (consolidated): judge Instant Form CPL with real data; cut cold ad set `120251560593780248` down to top 2–3 performing ads; compare cold vs retargeting CPL; assess whether the Jul 19 $20/day bump is paying off. Both ad sets restarted learning from zero Jul 19 — don't over-read numbers before this. Owner: agent.
6. **Booked-exclusion audience** `120251421422810248` still too small (code 300) — built on CompleteRegistration, can't grow until #2 is fixed. Recheck after pixel fix. Owner: agent.

## Weekly report
7. **Confirm the idempotency guard holds** — watch the Jul 20 scheduled run fires exactly once and behaves correctly.

## Content
8. **Week-2 blog post** — "Construction Loans in WA: How Progress Payments Actually Work", due ~Jul 20, still not started. Owner: agent. (Note: V3 Construction is the ad-delivery workhorse — post + ad angle reinforce each other.)
9. **FB organic post** — "$100,000 apart" creative + caption ready; Callum to publish. Owner: Callum.

## Skills/docs hygiene
10. **meta-ad-review SKILL.md stale** — still says HOUSING/CREDIT special ad category; settled decision is FINANCIAL_PRODUCTS_SERVICES. One-line fix. Owner: agent, on explicit ask (non-memory file).

## Carried forward (unchanged)
11. **generate_lead GA4 tagging** on booking confirmation — related to #2; needs Callum's go-ahead on approach.
12. **Purple Circle sign-off** on `.claude/AU-finance-compliance.md`. Owner: Callum.
13. **Privacy policy check** — Meta pixel remarketing coverage. Owner: Callum.
14. **product-marketing.md gaps** — metrics, verbatim customer language, named competitors.
15. **Optional cleanup** — 4 orphaned unbranded Canva creative objects in the Meta library. Low priority.

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
