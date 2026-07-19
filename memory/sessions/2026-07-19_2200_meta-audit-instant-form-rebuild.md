# Session — 2026-07-19 (evening) — galway-finance

## Objective
Run a full Meta ads audit (creative/compliance, performance, structure/tracking) for the two live serviceability campaigns, then execute the approved fixes: convert both campaigns to true Instant Form lead optimization.

## Summary
Started with `meta-report` (zero-lead streak continuing: active campaigns spent A$59.55 Jul 12–18 with 0 leads/conversions despite 14 LPVs) and confirmed via ad-set detail pulls that the setup was optimizing toward a website Lead pixel event that stopped firing at the Jul 15 relaunch. The full 7-ad audit found the human-written copy strong (V1–V4, V6–V7 pass the compliance checklist) but Meta's Advantage+ `text_optimizations` had generated 6 non-compliant auto-variants on V5 ("best deal", dropped disclosure line, alarmist framing) — a live compliance FAIL. Executed with Callum's approval: paused V5, built a clean single-body creative (LEARN_MORE, all enhancements disabled) and swapped it in; then converted the cold campaign to Instant Form — Meta blocked the in-place change (attribution immutable, subcode 1504040) and blocked coexisting goals in a lowest-cost CBO campaign (subcode 1885760), so the old ad set was archived and a new LEAD_GENERATION/ON_AD ad set created with all 5 ads. Repeated the same rebuild for retargeting with clean V6/V7 creatives, keeping warm audiences but aligning geo to Alkimos 50km per Callum. Booked-exclusion audience still too small (code 300) because its CompleteRegistration source event is also broken.

## Outcomes
- Full 7-ad audit: per-ad compliance/creative/policy scorecards + performance triage + structure findings; only compliance FAIL was V5's Meta-generated auto-variants
- Cold campaign → Instant Form: new ad set `120251560593780248` "Broad Perth — Instant Form leads" (LEAD_GENERATION/ON_AD, Alkimos 50km, 1d-click attribution, AUSTRALIA_FINSERV) with 5 ads (V1 `120251560594890248`, V2 `120251560595390248`, V3 `120251560596170248`, V4 `120251560596630248`, V5-clean `120251560597530248` / creative `2272244293522390`); old ad set `120251478141350248` archived
- Retargeting → Instant Form: new ad set `120251560809090248` "Retargeting — Instant Form leads" (warm audiences ECA 365d + WCA 90d kept, geo now Alkimos 50km) with clean V6 `120251560810320248` (creative `1819052822408345`) and V7 `120251560811000248` (creative `1545833923955545`); old ad set `120251478599480248` archived
- 3 clean creatives built: single compliant body, LEARN_MORE CTA, `disable_all_enhancements` — the pattern for all future regulated creatives
- Clarified for Callum how to verify the Lead pixel event in Events Manager (Test Events + 30-day trend + GTM trigger URL scope)

## Decisions
- **Lead path = Instant Form** on both campaigns (form `2234033924078396`), replacing website-conversion optimization. Reason: Callum wants softer higher-volume leads for database-building and calling practice; the website event was broken anyway.
- **Advantage+ enhancements always OFF on regulated creatives** (`disable_all_enhancements`). Reason: text_optimizations generated non-compliant V5 variants (dropped disclosure, "best deal").
- **Retargeting geo = Alkimos 50km** (matches broad campaign; geo only — warm audiences retained, no interests). Callum's call.

## Insights
- Advantage+ `text_optimizations` / `asset_feed_spec` variants can silently serve AI-rewritten copy that drops mandatory credit disclosures — audit `asset_feed_spec` for stored variants; primary copy alone won't show them. (importance 5)
- Meta locks `attribution_spec` and `optimization_goal` post-creation (1885560/1504040) and lowest-cost CBO requires one goal across ad sets (1885760). Conversion path: archive old ad set → create new-goal ad set → recreate ads pointing at existing creative IDs. LEAD_GENERATION needs 1d-click/0-view attribution.
- `promoted_object {pixel, LEAD}` + `WEBSITE_AND_LEAD_FORM` is a *valid* config — the earlier "should be LEAD_GENERATION" note was wrong as a diagnosis. Real causes: dead website event + form/optimization mismatch.
- Event-based audiences inherit tracking breakage: booked-exclusion WCA can't grow while CompleteRegistration is dead.
- Meta Graph API transient 500s: day-breakdown insights failed while plain aggregates succeeded on retry — fall back to weekly aggregates.

## Open loops
- Callum: set FINANCIAL_PRODUCTS_SERVICES special ad category on BOTH campaigns (Ads Manager; recheck ad-set targeting after — may reset)
- Callum: fix Lead/CompleteRegistration pixel events on the site (blocks exclusion audience + retargeting hygiene + GA4, not lead optimization anymore)
- Callum: review Instant Form 2234033924078396 (questions, privacy link, completion message) + confirm lead notifications for speed-to-call
- Verify all 7 new ads cleared Meta review (~24h); judge delivery only after 5–7 days learning
- Booked-exclusion audience `120251421422810248` still code 300 — recheck after pixel fix
- Week-2 blog post "Construction Loans in WA" due ~Jul 20 — still not started
- Confirm Jul 20 weekly report fires exactly once under the idempotency guard
- Callum: publish FB organic post ("$100,000 apart")
- meta-ad-review SKILL.md stale (says HOUSING/CREDIT; settled decision is FINANCIAL_PRODUCTS_SERVICES) — one-line fix pending
- Carried: Purple Circle sign-off; privacy policy pixel check; product-marketing.md gaps

## Artifacts
- New cold ad set `120251560593780248` + 5 ads (in Meta review)
- New RTG ad set `120251560809090248` + 2 ads (in Meta review)
- Clean creatives: `2272244293522390` (V5), `1819052822408345` (V6), `1545833923955545` (V7)
- Audit report delivered in-session (terminal only)

## Tools used
- startup, meta-report, meta-ad-review, wrap-up skills; Pipeboard Meta Ads MCP (read + write); Supabase MCP
