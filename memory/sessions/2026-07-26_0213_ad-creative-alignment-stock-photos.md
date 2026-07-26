# Session — 2026-07-26 — galway-finance

## Objective
Recreate the 7 Meta ad cards as individual Claude Design pages, align them to Callum's existing Meta Ad Templates visual system, and source real stock photography for the two photo-based ads.

## Summary
Built a new Claude Design project ("Galway Finance — Meta Ads") with all 7 ads as separate pages. Callum then pointed out an existing "Meta Ad Templates.dc.html" reference system (in the "Social media ad templates" project) with a much richer, already-established visual language — distinct color palette (#0D1356/#181E87/#A3A9F8), Outfit/Poppins type, eyebrow pills, ghost-numeral question motifs, stat blocks, and photo+plate layouts — that the session's earlier ring-motif redesign did not match. Rebuilt all 7 ads to align with this system, mapping each ad to the best-fit layout pattern (bold statement, qualifying question, stat hero, or photo+plate) while preserving every headline/support copy string verbatim.

Discovered and adopted the `<image-slot>` web component the reference system already uses for photos — a real drag-and-drop placeholder in the Claude Design canvas — which sidesteps the image-gen API gap found earlier in the session entirely. For the two photo ads (V2, V6), no `search_stock_photos` tool or stock-photo API was available, so sourced candidates manually via web search across several rounds (a too-upscale architect-designed home, then modest options that were geographically North-American-coded), and Callum ultimately chose to accept the polished/upscale matched pair (same photographer, same shoot) over the modest-but-mismatched alternatives. Set both photos via the image-slot `src`/`credit` attributes and verified via screenshot that both render correctly with attribution.

## Outcomes
- All 7 Meta ads rebuilt and visually aligned to the existing Meta Ad Templates system in Claude Design, copy unchanged
- Real stock photography (Pexels, same photographer/shoot) now live in the V2 and V6 image-slot placeholders, with credit overlay
- Confirmed `<image-slot>` works standalone (outside the full design-doc wrapper) and resolves the earlier "no image-gen API" blocker for future photo-based ad creative

## Decisions
- **Ad creative visual system**: align to the existing "Meta Ad Templates.dc.html" system (Social media ad templates project), not the older ring-motif cards in the base design system — that system is now superseded.
- **Photo placeholders use image-slot, not an image-gen API**: drag-and-drop in the Claude Design canvas, no code/API needed.
- **V2/V6 stock photo choice**: accepted the upscale/architect-designed matched pair (same photographer/shoot) over modest-but-North-American-coded alternatives.

## Insights
- Canonical Meta ad visual system: "Social media ad templates" project (`e5106aea-b312-446d-b2b9-49175d1de155`), file "Meta Ad Templates.dc.html" — 7 reference layouts on the brand palette. Check this first before designing new Meta ad creative.
- No `search_stock_photos` tool or stock-photo API configured — `<image-slot>` falls back cleanly to manual drag-and-drop, a real working solution.
- Pexels (and free stock generally) skews North-American for "ordinary suburban house" imagery — real tradeoff between economic-tier accuracy and geographic authenticity for AU-specific creative. Pixabay returns 403 to WebFetch, not usable this way.

## Open loops
- Push the 7 aligned ad designs into live Meta ad creatives (`ads_creative_upload_image` + `ads_create_creative`/`ads_update_entity`) — designs finished, not deployed
- Low-priority cleanup: remove/archive the superseded ring-motif ad cards in the base Galway Finance Design System's `ads/` folder
- Stock photo tone tradeoff accepted (V2/V6 house reads upscale) — revisit if it becomes a real concern once ads are live
- Carried from earlier this session: confirm RTG campaign pause + Test-Broad-Australia ad-set pause were intentional; push drafted ad-copy fix to disapproved ad `120251618482150248`; Instant Form UX audit + missing `privacy_policy_url`; `special_ad_category` fix on both live campaigns

## Artifacts
- Claude Design — "Galway Finance — Meta Ads" (aligned + photographed): https://claude.ai/design/p/0efb615c-c7bd-4450-b0c5-2257eeec3fd4

## Tools used
- mcp__claude-design__*
- mcp__claude-in-chrome__* (visual verification)
- WebSearch, WebFetch
