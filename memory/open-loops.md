# Open loops — galway-finance

*Updated 2026-07-19 (Meta audit + Instant Form rebuild session)*

## Meta ads
1. **Special ad category (both campaigns)** — set `FINANCIAL_PRODUCTS_SERVICES` on cold `120251478141370248` AND retargeting `120251478599460248` in Ads Manager (API can't set post-creation). After applying, recheck the new ad sets' targeting — Meta may reset some of it. Owner: Callum.
2. **Fix Lead/CompleteRegistration pixel events** on the site — no longer blocks lead optimization (both campaigns now Instant Form), but blocks: booked-exclusion audience growth, retargeting hygiene, GA4 lead visibility. Check Events Manager Test Events on `/new-home-borrowing-power/` + GTM trigger URL scope (event fired under old campaign, 0 times since Jul 15 relaunch). Owner: Callum.
3. **Instant Form review** — check form `2234033924078396` questions, privacy policy link, completion message; confirm lead notifications (Leads Center/email) reach Callum for fast follow-up calls. Owner: Callum.
4. **Verify 7 new ads clear Meta review** (~24h from Jul 19 evening): cold ad set `120251560593780248` (V1–V5), RTG ad set `120251560809090248` (V6–V7 clean). Owner: agent (next session check).
5. **Judge delivery only after 5–7 days** — both ad sets restarted learning from zero Jul 19. Don't over-read early numbers. Owner: agent.
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

## Resolved this session
- ~~Zero-lead streak root cause~~ — dead website Lead event + optimization/destination mismatch; fixed by converting both campaigns to Instant Form (LEAD_GENERATION/ON_AD).
- ~~V5 compliance FAIL~~ — Meta text_optimizations auto-variants ("best deal", dropped disclosure) killed via clean single-body creative rebuild.
- ~~Cold duplicate Instant Form setup~~ — done properly via new ad set `120251560593780248` (old one archived).
- ~~Retargeting Perth-40km geo~~ — aligned to Alkimos 50km per Callum (warm audiences kept).
- ~~Weak SEE_DETAILS CTA~~ — LEARN_MORE on rebuilt V5/V6/V7 creatives (V1–V4 keep SEE_DETAILS by scope choice).
