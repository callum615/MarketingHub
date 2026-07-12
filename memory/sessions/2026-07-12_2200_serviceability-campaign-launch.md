# Session — 2026-07-12 22:00 AWST — galway-finance

## Objective
Build and launch a new A$20/day Meta ad campaign for Galway Finance focused on lender serviceability differences for new-home buyers, replacing the fatigued New Homes campaign.

## Summary
Picked "new homes + serviceability" as the campaign angle, staged a compliance-checked WordPress landing page, and wrote 5 ad copy variants. Iterated through three creative directions (Canva-generated, then Claude Design HTML/CSS cards) before landing on a "circle hybrid" style blending the client's previous campaign's signature navy+circle-photo layout with modern typography, at the user's request to combine "modern" with "the existing ad style I had in my previous campaign." Built all 5 variants as reusable HTML cards in the Galway Finance Design System, rendered them to exact 1080x1350 PNGs via headless Chrome, and uploaded to Meta via a catbox.moe URL bridge (the browser's file-upload tool and inline base64 transfer were both infeasible for images this size in this harness). Found 3 of 5 ads had come back DISAPPROVED from Meta's review of the earlier Canva creative; root-caused to the landing page still being an unpublished draft. User published the page; disapprovals cleared on the fresh creative set. Paused the old "New Homes Campaign" (A$25/day, HOUSING category) and activated the new campaign (A$20/day, FINANCIAL_PRODUCTS_SERVICES category) with all 5 ads set to ACTIVE.

## Outcomes
- Landing page live: https://galwayfinance.com.au/new-home-borrowing-power/ (WP page 53) — serviceability angle, FAQ schema, CRN 579221 disclosure
- 5 Meta ad creatives built in "circle hybrid" style, stored as reusable HTML cards in Galway Finance Design System ("Ads" group)
- New Meta campaign live: META_Leads_Broad-Perth_Serviceability-LP_2026-07 (120251395173300248), A$20/day, ACTIVE, FINANCIAL_PRODUCTS_SERVICES category
- Old New Homes Campaign (120251239987690248) paused — A$25/day spend stopped
- 4 of 5 new ads passed Meta review after landing page published; hero (V1) pending review at session end

## Decisions
- Serviceability angle (lender borrowing-power differences) chosen over refinance/generic FHB — defensible, compliance-friendly, concrete local hook
- Circle-hybrid creative direction chosen over full-bleed-photo and solid-band alternatives — keeps continuity with the previous campaign's recognizable navy+circle signature while modernizing typography
- Ad creatives built in Claude Design (HTML/CSS cards) instead of Canva going forward — pixel-exact, brand-token-driven, instantly reusable/iterable
- All future Galway Finance Meta campaigns must use special_ad_category FINANCIAL_PRODUCTS_SERVICES, not CREDIT (Meta retired CREDIT — fails with error_subcode 2909060)

## Insights
- Meta DISAPPROVES (not just holds pending) ads linking to an unpublished WordPress draft landing page — the crawler can't validate a draft/404 destination. Publish landing pages before ads referencing them go live.
- claude-in-chrome's file_upload tool no longer accepts local filesystem paths in this harness version. Bridge local images to Meta via curl-upload to catbox.moe (anonymous, no auth) for a public URL, then Meta's bulk_upload_ad_images with image_url — avoids inflating context with base64.
- DesignSync (Claude Design) write_files with localPath reads from disk without content entering the model's context — the only low-cost bulk-file mechanism available; Meta Ads/Google Drive/WordPress media tools all require inline base64, expensive for images over ~100KB.
- Headless Chrome (`--headless=new --window-size=WxH --force-device-scale-factor=1 --screenshot=out.png`) gives pixel-exact renders of local HTML/CSS designs — more reliable than the interactive browser tool's auto-scaling screenshot/zoom actions for exact-dimension asset export.

## Open loops
See `memory/open-loops.md` (updated this session).

## Artifacts
- WP page 53 — https://galwayfinance.com.au/new-home-borrowing-power/ (published)
- Meta campaign 120251395173300248 — META_Leads_Broad-Perth_Serviceability-LP_2026-07
- Meta ad set 120251395176490248, 5 ads (120251395186600248, 120251395187140248, 120251395187900248, 120251395189720248, 120251395193710248)
- Claude Design System project 63603262-f698-4cbb-88c9-9164ce140eb6 — "Ads" group, 5 circle-hybrid card files

## Tools used
- wp-publish skill, ad-creative skill, ads skill, WordPress.com MCP, Pipeboard Meta Ads MCP, Claude Design (DesignSync), Canva MCP, headless Chrome (local), catbox.moe
