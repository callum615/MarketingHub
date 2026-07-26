# Open loops — galway-finance

*Updated 2026-07-26 (early hours) — ad creative aligned to Meta Ad Templates system + stock photos sourced. This worktree's local memory was 4 days stale as of 2026-07-25; reconstructed from Supabase, which is source of truth.*

## Meta ads — needs Callum confirmation
0. **RTG retargeting campaign is now fully CAMPAIGN_PAUSED** (`120251478599460248`) — previously logged as "ACTIVE but dark 5+ days," now paused at the campaign level. Confirm this was intentional; if not, it's most of the account's warm-audience reach gone quiet. Owner: Callum.
0b. **Test-Broad-Australia ad set is now fully ADSET_PAUSED** (all ads except the still-disapproved V1) — confirm intentional. Owner: Callum.

## Meta ads — in progress
1. **Push drafted compliant ad-copy rewrite to disapproved ad** `120251618482150248` (V1 Two Lenders hero, Test-Broad-Australia) via the native Meta connector (`ads_create_creative` + `ads_update_entity`). Copy is ready (removed the "no credit check" trigger phrase, fixed a hyper-local claim). Was blocked by Pipeboard's execution cap; native connector is now live and unblocked. Owner: agent.
2. **Instant Form UX audit** — nobody has reviewed the live form's (`2234033924078396`) actual question flow, friction, or completion message since the Jul19 Instant Form rebuild. Do this before concluding the zero-lead streak is a pure demand problem. Owner: agent.
3. **Instant Form missing `privacy_policy_url`** — confirmed empty via API. Compliance gap (not believed to block submissions technically, but still needs fixing). Owner: Callum/agent.
4. **special_ad_category mismatch** — both live campaigns still don't match the settled `FINANCIAL_PRODUCTS_SERVICES` (currently HOUSING / unset). API can't set post-creation — Ads Manager only. Owner: Callum.
5. **Define a target CPL or lead-volume goal** for the Meta campaigns — still no number in memory to judge go/no-go decisions against. Owner: Callum.
6. **Zero-lead streak** — now 10+ consecutive days across all campaigns despite Instant Form conversion (since the Jul19 rebuild). $170.28 spent this week (Jul19-25) alone. Treat as a stop-and-diagnose moment (form UX audit, not another wait cycle) before considering a full campaign pivot — account has been restructured 4+ times in 2 weeks, so "concept doesn't work" isn't a clean read yet. Owner: agent/Callum.
7. **ads_get_errors tool broken** in this environment — resolver error on every entity ID tried. Use `effective_status`/`delivery` substatus from `ads_get_ad_entities` instead until fixed. Owner: agent (workaround only, not a real fix).

## Ad creative refresh (Claude Design)
8. ~~Source real photography~~ — **done 2026-07-26**. No image-gen API available, but the `<image-slot>` component (drag-and-drop in the Claude Design canvas) solved it without one. V2 and V6 now have real Pexels stock photos (same photographer/shoot) set via `src`/`credit`.
9. **Push the aligned ad designs into live Meta ads** — all 7 ads in the "Galway Finance — Meta Ads" project (https://claude.ai/design/p/0efb615c-c7bd-4450-b0c5-2257eeec3fd4) are finished: aligned to the existing Meta Ad Templates visual system, copy verbatim, photos in place. Needs `ads_creative_upload_image` + `ads_create_creative`/`ads_update_entity` to go live. Owner: agent, on Callum's go-ahead.
10. **Cleanup — superseded ring-motif ad cards** — the first-pass redesign in the base Galway Finance Design System's `ads/` folder (meta-hero.card.html etc.) is now superseded by the aligned versions in "Galway Finance — Meta Ads". Low priority: remove or archive. Owner: agent, on explicit ask.
11. **Stock photo tone tradeoff** — V2/V6 house reads more upscale/architect-designed than a typical client's home; Callum accepted this consciously over geographically-mismatched modest alternatives. Revisit only if it becomes a real concern once ads are live.
10. **Optional cleanup** — 3 now-unused stock photos (`fhb-entrance.jpg`, `house-dusk.jpg`, `quote-pathway.jpg`) still in the design system, left in place for comparison. Low priority.

## Weekly report
11. **Confirm the idempotency guard holds** — watch scheduled runs fire exactly once and behave correctly.

## Content
12. **Week-2 blog post** — "Construction Loans in WA: How Progress Payments Actually Work", due Jul20 — still overdue, still not started. Owner: agent. (V3 Construction is the ad-delivery workhorse — post + ad angle reinforce each other, though V3 is currently paused.)
13. **FB organic post** — "$100,000 apart" creative + caption ready; Callum to publish. Owner: Callum.

## Skills/docs hygiene
14. **meta-ad-review SKILL.md stale** — still says HOUSING/CREDIT special ad category; settled decision is FINANCIAL_PRODUCTS_SERVICES. One-line fix. Owner: agent, on explicit ask.

## Referral network (Jul21 plan, largely untouched since)
15. Rank existing loose contacts by type/warmth (was due Jul22)
16. Confirm referral-relationship structure with Purple Circle (reciprocal only, no fees tied to loan value/volume) (was due Jul23)
17. Draft the standard "what's in it for you" one-liner for partners (was due Jul23)
18. Build target prospect list (5-8 per type) across Perth metro (was due Jul25)
19. Create the partner one-pager (was due Jul25)
20. Full 12-task plan tracked in Notion "Referral Network Plan - Progress" (Marketing Hub) — check there for current status, this list may be stale.

## Carried forward (unchanged)
21. **Purple Circle sign-off** on `.claude/AU-finance-compliance.md`. Owner: Callum.
22. **Privacy policy check** — Meta pixel remarketing coverage. Owner: Callum.
23. **product-marketing.md gaps** — metrics, verbatim customer language, named competitors.
24. **GA4 hygiene from 2026-07-21 audit**: three phantom conversion events (`purchase`, `close_convert_lead`, `qualify_lead`) marked as conversions but never fired — safe to unmark. Consider marking `calculator_cta_click`/`contact_cta_click` as key events, add a custom dimension for loan-type/page-category. Low priority.
25. **Confirm a real Calendly booking produces the Lead event end-to-end** in Meta Events Manager + GA4 — the Jul21 tracking fix's code path is proven but production has not been observed yet.

## Resolved this session (Jul25 afternoon)
- ~~Redesign ad creative visuals to remove photo dependency~~ — 5 of 7 Meta ad cards rewritten in Claude Design; graphic-only ring/typography treatment, copy preserved.
- ~~Diagnose whether a campaign pivot is warranted~~ — advised against it for now; recommended Instant Form UX audit + letting the account stabilize first.

## Resolved earlier (Jul23-25, reconstructed from Supabase)
- ~~Reconnect Meta Ads access after Pipeboard cap/disconnect~~ — Pipeboard fully decommissioned; native `mcp__claude_ai_Meta__*` connector confirmed live 2026-07-25.
- ~~Root-cause the disapproved ad~~ — "no credit check" trigger phrase + text_optimizations OPT_IN; compliant rewrite drafted 2026-07-25 (push still pending, see #1 above).
- ~~Confirm broader-Australia targeting + budget cut were intentional~~ — confirmed 2026-07-23, tied to Callum's possible relocation.
- ~~Execute Jul24-26 checkpoint ad-count cut~~ — done early, 2026-07-23 (V3/V5 paused, V1/V2/V4 kept active).
