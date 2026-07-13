# Session — 2026-07-13 23:00 AWST — galway-finance

## Objective
Build a Meta retargeting layer (audiences, campaign, ad set, creatives, ads) to re-engage warm traffic from the serviceability campaign.

## Summary
Day-1 serviceability campaign results were strong (634 impressions, 3.8% CTR, 10 link clicks, 7 LP views, A$24.40 spend). Planned and built a full retargeting stack: 3 custom audiences (site visitors 90d, FB Page engagers 365d, booked-leads exclusion 180d), a separate ABO campaign at A$5/day, and two new warm-audience circle-hybrid creatives (V6 reminder, V7 next-step) built in the design system, rendered via headless Chrome (reusing the Jul 12 session's surviving dsbuild bundle in tmp), bridged to Meta via catbox.moe. Everything created PAUSED per the publishing gate. Meta's Custom Audience ToS gating took two rounds of browser acceptance by Callum (custom_audience_tos via the tos URLs, then web_custom_audience_tos via the Ads Manager Create Audience UI). Pipeboard's free-plan weekly limit hit on the final update_adset call; Callum attached the website audiences manually in Ads Manager (not yet API-verified).

## Outcomes
- Retargeting campaign `META_Leads_RTG-Perth_Serviceability-LP_2026-07` (120251420896860248) — PAUSED, FINANCIAL_PRODUCTS_SERVICES (AU), ad-set budgets
- Ad set 120251421081140248 — A$5/day, OFFSITE_CONVERSIONS/CompleteRegistration on pixel 1326281722330947, Perth+40km, audience expansion disabled
- 3 custom audiences (account's first): ECA FB engagers 365d (120251420871500248), WCA site visitors 90d (120251421421940248, prefilled), WCA booked exclusion 180d (120251421422810248)
- 2 ads PAUSED in Meta review: RTG V6 Reminder (120251421115940248), RTG V7 Next step (120251421115710248) — BOOK_NOW CTA, CRN 579221 disclosure, UTM `rtg-serviceability-2026-07`
- V6/V7 cards added to Design System "Ads" group (meta-rtg-v6-reminder / meta-rtg-v7-nextstep)

## Decisions
- Retargeting runs as a **separate A$5/day ABO campaign**, not an ad set inside the live A$20/day CBO campaign — CBO would starve the small warm audience; keeps live campaign untouched and reporting clean
- Audience definition: site visitors 90d + FB Page engagers 365d (OR), excluding CompleteRegistration 180d
- Warm audiences get **dedicated creative** (reminder + objection angles), not reused cold creatives
- All new spend objects created PAUSED; Callum activates (publishing-gate consistency)
- Report retargeting CPL separately from cold CPL — warm CPL will look artificially cheap

## Insights
- Meta gates Custom Audience creation on TWO ToS docs × two scopes: the tos URLs grant only `custom_audience_tos`; WEBSITE-subtype audiences also need `web_custom_audience_tos`, granted only via Ads Manager → Create Audience → Website UI flow as the OAuth user (error 2663 until then). ENGAGEMENT audiences need neither.
- Meta silently enables Advantage custom audience expansion (`targeting_relaxation_types.custom_audience=1`) on ad set creation — delivery goes beyond the warm audience. Explicitly set `{lookalike:0, custom_audience:0}` for pure retargeting and verify.
- Pipeboard free plan has a weekly command limit that blocks reads AND writes mid-workflow without warning. Manual Ads Manager edits are the fallback.
- Session scratchpads under `/private/tmp/claude-501/<project>/<session>/` persist across sessions — the Jul 12 dsbuild bundle (tokens, logos, cards) was reused directly.
- The **live** campaign's `special_ad_categories` reads `[]` via the same API call that correctly echoes the new campaign's category — likely genuinely missing on the live campaign; policy risk, flagged to Callum.

## Open loops
See `memory/open-loops.md` (updated this session).

## Artifacts
- Meta campaign 120251420896860248 / ad set 120251421081140248 / ads 120251421115940248, 120251421115710248
- Audiences 120251420871500248, 120251421421940248, 120251421422810248
- Design System project 63603262-f698-4cbb-88c9-9164ce140eb6 — ads/meta-rtg-v6-reminder.card.html, ads/meta-rtg-v7-nextstep.card.html

## Tools used
- Pipeboard Meta Ads MCP, DesignSync, headless Chrome, catbox.moe, Supabase MCP, startup/wrap-up skills, plan mode
