# Session — 2026-07-25 — galway-finance

## Objective
Pull the weekly Meta Ads report via the new native connector, advise on whether a campaign pivot is warranted, and rebuild the Meta ad creative images in the Galway Finance Design System.

## Summary
Ran meta-report for Jul19-25 via the native Meta connector (Pipeboard fully retired): $170.28 spent vs $59.55 prior week, zero leads both weeks, CPC nearly tripled ($2.84 → $8.51). Discovered two undocumented status changes not yet in memory: the RTG retargeting campaign is now fully CAMPAIGN_PAUSED (not just dark), and the entire Test-Broad-Australia ad set is now ADSET_PAUSED except the still-disapproved V1 ad — only 3 ads live account-wide. `ads_get_errors` failed on every entity ID tried (resolver error), unusable this session.

Callum asked whether it's too early to pivot to a new campaign; advised no — the account has been restructured 4+ times in two weeks (resets learning each time) and the Instant Form itself has never been UX-audited, both cheaper diagnostics than a full pivot. Corrected an overstated claim that the missing `privacy_policy_url` causes zero submissions — no real mechanism for that, it's a compliance gap not a technical blocker.

Callum then asked to redo the ad images via Claude Design. Found no image-gen API (Flux/Gemini/Ideogram) configured and Canva MCP is templated-design-only, so real photography can't be generated in this environment yet — flagged the gap rather than faking a workaround. Callum chose to redesign all 7 ad cards now to a graphic-only ring/typography treatment (no photo, no people) matching the existing V4/V7 style, with real photography to be swapped in later once sourced. Rewrote 5 of 7 cards accordingly, preserved all headline/support copy verbatim (one domain mention relocated for consistency), verified 2 renders via browser screenshot and fixed a headline-wrap issue on V1.

## Outcomes
- Meta report delivered in-session (Jul19-25): $170.28 spend, 0 leads, CPC +200% WoW
- Found RTG campaign now fully CAMPAIGN_PAUSED and Test-Broad-Australia ad set now ADSET_PAUSED — both undocumented, need Callum confirmation
- Redesigned 5 of 7 Meta ad cards in Claude Design (Ads group) to remove photo dependency: `meta-hero.card.html`, `meta-hero-v2-fhb.card.html`, `meta-hero-v3-construction.card.html`, `meta-hero-v5-quote.card.html`, `meta-rtg-v6-reminder.card.html`
- Verified 2 card renders via browser screenshot; fixed a headline-wrap bug on the V1 hero card

## Decisions
- **Ad creative refresh approach**: redesign all 7 cards now to graphic-only ring/typography (no photo), reusing V4/V7 style; add real photography later. Reason: no image-gen API configured, Canva MCP can't produce standalone photos.
- **New ad photography direction**: property/lifestyle only, no people/faces, once sourced. Reason: matches existing style, avoids AU credit-ad compliance risk (NCCP/ASIC) around AI images implying a real customer/testimonial.

## Insights
- `ads_get_errors` (native Meta connector) is currently broken in this environment — "Could not resolve an ad account from entity_ids" on every ID tried. Use `effective_status`/`delivery` substatus fields from `ads_get_ad_entities` instead.
- No image-generation API (Gemini/Flux/Ideogram) configured — no env vars found. Canva MCP only does templated designs with baked-in text/layout.
- Account restructured 4+ times in 2 weeks (budget, ad-count, targeting, RTG pause, Test-Broad-Australia pause) — each resets Meta's learning phase. Don't over-read "concept doesn't work" until a stable week happens.
- RTG campaign (`120251478599460248`) now CAMPAIGN_PAUSED at the campaign level; Test-Broad-Australia ad set fully ADSET_PAUSED except the disapproved V1. Neither explained in memory — confirm with Callum.
- Missing Instant Form `privacy_policy_url` is a compliance gap, not a technical submission blocker — don't cite it as a likely cause of zero leads without a real mechanism.

## Open loops
- Confirm whether RTG campaign pause and Test-Broad-Australia ad-set pause were intentional
- Push drafted compliant ad-copy fix to disapproved ad `120251618482150248` via native connector — still not executed
- Audit the live Instant Form (`2234033924078396`) question flow/UX/completion message — never done since Jul19 rebuild
- Fix missing `privacy_policy_url` on the Instant Form
- Set `special_ad_category` to `FINANCIAL_PRODUCTS_SERVICES` on both live campaigns (Ads Manager only)
- Source real photography (API key for Flux/Gemini/Ideogram, or manually supplied photos) to complete the circle-crop treatment
- Push redesigned ad card images into live Meta ad creatives once photography is finalised (`ads_creative_upload_image` + `ads_create_creative`/`ads_update_entity`)
- Week-2 blog post ("Construction Loans in WA") still overdue since Jul20
- Optional cleanup: 3 unused stock photos (`fhb-entrance.jpg`, `house-dusk.jpg`, `quote-pathway.jpg`) left in the design system

## Artifacts
- Claude Design — Galway Finance Design System, Ads group: 5 rewritten cards. https://claude.ai/design/p/63603262-f698-4cbb-88c9-9164ce140eb6?file=ads%2Fmeta-hero.card.html
- Meta ads report Jul19-25 — delivered in-session (terminal only, not persisted to Notion per ad-hoc rule)

## Tools used
- mcp__claude_ai_Meta__* (native connector)
- mcp__claude_ai_Supabase__*
- mcp__claude-design__*
- mcp__claude-in-chrome__* (render verification)
- image skill (surfaced capability gap)
