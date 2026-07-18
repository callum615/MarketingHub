# Session — 2026-07-18 — galway-finance

## Objective
Run a Meta ad account health sweep, fix retargeting issues found, confirm the week-1 blog post's status, and produce an organic Facebook post (copy + Canva creative) to promote it.

## Summary
Pushed a pending memory commit, then ran a full Meta Ads health check: found the live cold campaign's ad set had been silently paused since Jul 15 (zero delivery for 3 days) and traced it to Callum having duplicated both the cold and retargeting campaigns that night to rework objectives/geo. Fixed the retargeting duplicate's targeting (attached the now-large-enough WCA site-visitors audience alongside the existing FB engagers audience, disabled Advantage+ audience expansion) and verified it live via API. Archived both original campaigns per Callum's call. Confirmed the cold duplicate's Alkimos/50km geo was a deliberate northern-suburbs targeting choice, not a bug, and confirmed its Instant Form objective change is only partially done (Callum finishing it himself) and still lacks a special_ad_category declaration. Verified the week-1 blog post ("How Much Can I Borrow?") is actually already published, correcting a stale open-loop. Built an organic Facebook post to promote it: drafted two compliant caption options, then iterated a Canva creative through several rounds (discovering that passing the brand logo as an asset to Canva's generate-design tool causes it to skip stock photos entirely) before landing on a version with a real lifestyle photo, the Galway Finance logo, and modern/sleek typography. Callum has since made his own edits to the creative and the final caption is set.

## Outcomes
- Retargeting ad set (120251478599480248) targeting fixed live: WCA site-visitors 90d + ECA FB engagers attached, Advantage+ expansion disabled, targeting_relaxation_types confirmed {lookalike:0, custom_audience:0}
- Archived original cold campaign (120251395173300248) and original retargeting campaign (120251420896860248) now that Jul-15 duplicates are the live versions
- Confirmed week-1 post "How Much Can I Borrow?" is live at /resources/how-much-can-i-borrow/ (was stale as an open loop since Jul 12)
- FB organic post ready: Canva creative "Couple Engaged Over Kitchen Table Work" (DAHPtrfQk2I, real photo + logo, edited further by Callum) paired with a compliant "$100,000 apart" caption
- Pushed pending Jul-13 memory commit to origin (was 1 commit ahead)

## Decisions
- Archived both original Meta campaigns; duplicates are now the live versions.
- Cold duplicate's Alkimos/50km geo is intentional (covers northern Perth suburbs) — not a bug, no fix applied.
- FB organic creative direction: real lifestyle stock photo + logo, modern/sleek editorial style (distinct from the paid-ad circle-hybrid system).

## Insights
- Canva `generate-design`: passing a logo/brand asset via `asset_ids` makes the AI treat it as the sole image and skip stock photos entirely, even when explicitly prompted for a photo. Workaround: generate without `asset_ids` first, verify a real photo landed via `start-editing-transaction`, then insert the logo afterward via `insert_fill`.
- Always verify Canva `generate-design` output via `start-editing-transaction` (inspect `fills`/`richtexts`) before telling the user an asset is present — titles/thumbnails alone aren't reliable; two consecutive generations silently omitted the requested photo.
- Meta campaigns can show `configured_status: ACTIVE` while the ad set underneath is `effective_status: PAUSED` — this silently halts delivery/spend without the campaign looking paused. Check ad set-level status directly when diagnosing a performance drop.
- Meta custom audiences move from `delivery_status` 300 ("too small") to 200 ("ready") as matched users accumulate — recheck previously-blocked audiences periodically rather than assuming permanent failure.

## Open loops
- Cold duplicate campaign (120251478141370248): set special_ad_categories (FINANCIAL_PRODUCTS_SERVICES) in Ads Manager — can't be added via API post-creation. Owner: Callum.
- Cold duplicate: finish true Instant Form setup (optimization_goal still OFFSITE_CONVERSIONS, not LEAD_GENERATION). Owner: Callum.
- Watch cold duplicate CTR (0.46% vs original's 4.35%) over the next few days — Alkimos/northern-suburbs audience may just need time to warm up.
- Re-check WCA booked-exclusion audience size in a few weeks — still too small (delivery_status 300) to attach to retargeting.
- Draft week-2 post "Construction Loans in WA: How Progress Payments Actually Work" — due ~Jul 20, not started.
- GA4 generate_lead event on booking confirmation — still needs Callum's go-ahead on approach.
- Weekly-report cron still double-firing — needs a check in the Claude Code web UI trigger config.
- Privacy policy check for Meta pixel remarketing, and Purple Circle sign-off on AU-finance-compliance.md — both still outstanding.
- product-marketing.md gaps (metrics, verbatim customer language, named competitors) — still unfilled.

## Artifacts
- Meta campaign (archived): META_Leads_Broad-Perth_Serviceability-LP_2026-07 (120251395173300248)
- Meta campaign (archived): META_Leads_RTG-Perth_Serviceability-LP_2026-07 (120251420896860248)
- Meta campaign (active): cold duplicate 120251478141370248
- Meta campaign (active): retargeting duplicate 120251478599460248, ad set 120251478599480248
- Canva design: "Couple Engaged Over Kitchen Table Work" (DAHPtrfQk2I) — https://www.canva.com/d/PymsJe7n7ElX8w5
- Blog post (confirmed live): https://galwayfinance.com.au/resources/how-much-can-i-borrow/

## Tools used
- Supabase MCP, git/GitHub, Pipeboard Meta Ads MCP, WordPress.com MCP, Canva MCP
