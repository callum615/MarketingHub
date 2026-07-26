# Session — 2026-07-26 — galway-finance

## Objective
Push the 7 aligned Meta ad designs live and get copies saved to the Notion Marketing Hub.

## Summary
Investigated pushing the redesigned ads onto the live Meta ads — confirmed via a full tool audit that ad creatives are immutable via API and the creative-creation tool has no Instant Form parameter, so no safe automated path exists; a manual Ads Manager creative swap is the only way to preserve each ad's Instant Form attachment. Pulled and preserved the real live primary text/headline/CTA for all 7 ads (rich, compliance-reviewed multi-paragraph copy, distinct from the on-image text, previously undocumented in memory). Exported all 7 designs as clean full-resolution PNGs via a calibrated browser screenshot-stitch pipeline (Claude Design pages block scrolling via `overflow:hidden` — worked around with an injected JS override, then calibrated the viewport-to-CSS-pixel scale empirically with a marker element).

Attempted to get the images into Notion: WordPress-as-bridge hit a rate limit, direct browser upload into Notion's UI hit an app-deep-link redirect loop (worked around via JS-dispatched click) but then had trouble reliably creating new blocks and the browser session dropped entirely. Determined inline base64 upload (WordPress, Notion, Claude Design, Google Drive) is impractical at any real image quality — roughly 1 token per base64 character, so one compressed image alone would cost 100k+ tokens. Landed on the pragmatic solution: created a Notion page with context and the Claude Design link, and Callum will drag the 7 exported PNGs in manually.

## Outcomes
- Confirmed no safe API path exists to swap images on live Meta ads without losing Instant Form attachment — manual Ads Manager edit required
- Pulled and preserved the real live primary text/headline/CTA copy for all 7 ads (was previously undocumented)
- Exported all 7 ad designs as clean 1080×1350 PNGs via a working screenshot-stitch pipeline
- Created Notion page "Meta Ad Creative — Aligned Set (2026-07-26)" in Marketing Hub with context + Claude Design link

## Decisions
- **Meta creative deployment method**: no automated swap — Callum manually duplicates each ad in Ads Manager, replaces the image, publishes paused for review. API creative creation has no Instant Form parameter and would risk silently downgrading Instant Form ads to link-click ads.
- **Image delivery to Notion**: Callum manually drags the 7 PNGs in. Inline base64 is prohibitively expensive (~1 token/char); automated browser upload proved unreliable within reasonable effort.

## Insights
- Meta ad creatives are immutable via the native connector — `ads_creative_update` can't touch media/copy, `ads_create_creative` has no `lead_gen_form_id`/Instant Form field anywhere in its schema. Always route Instant Form ad creative changes through manual Ads Manager edit.
- Live Meta ad primary text (body) is rich, compliance-reviewed, multi-paragraph copy — entirely separate from the on-image headline/support text. Always pull via `ads_get_creatives` before touching any ad.
- **Inline base64 file upload is impractical everywhere** (WordPress media.create, Notion create-attachment, Claude Design write_files, Google Drive create_file) — ~1 token per base64 char, so a ~100KB image costs 100k+ tokens through agent context. For future binary-to-SaaS transfers: use a pre-existing public URL (server-side fetch, no context cost) or `mcp__claude-in-chrome__file_upload` (reads from disk by path, no context cost) — never inline base64.
- Notion's attachment API has no inline-binary path for non-text files — `source_url` (public) is the only option. "Just use the Notion MCP" doesn't bypass this; it's a Notion API constraint.
- Notion in this browser defaults to a native-app deep-link redirect that can loop on a plain click of "continue in browser" — dispatching `.click()` via injected JS on the actual anchor bypasses it when direct clicks don't.
- Claude Design pages with `overflow:hidden` block `window.scrollTo` for screenshot capture — override via injected JS temporarily. Browser screenshot viewport doesn't map 1:1 to CSS pixels here — calibrate the scale empirically with a marker element, don't trust `devicePixelRatio`/`innerWidth`/`innerHeight` directly. `render_preview` URLs expire in ~1hr.

## Open loops
- Callum: drag the 7 PNGs from `/tmp/meta_ads_final/` into the Notion "Meta Ad Creative — Aligned Set" page (files are in system temp, not durable — re-export from Claude Design if lost)
- Manual Ads Manager creative swap needed to push new images live on: V1 `120251560594890248`, V2 `120251560595390248`, V3 `120251560596170248`, V4 `120251560596630248`, V5 `120251560597530248`, RTG V6 `120251560810320248`, RTG V7 `120251560811000248` — duplicate ad, replace image, keep Instant Form identical, publish paused
- Build 1:1 square and 9:16 Stories/Reels format versions of all 7 ads (confirmed wanted earlier this session)
- Carried: RTG campaign pause + Test-Broad-Australia pause confirmation, disapproved ad `120251618482150248` copy fix, Instant Form UX audit + missing `privacy_policy_url`, `special_ad_category` fix on both live campaigns

## Artifacts
- Notion — "Meta Ad Creative — Aligned Set (2026-07-26)": https://www.notion.so/Meta-Ad-Creative-Aligned-Set-2026-07-26-3a9c844e9c4381a5a20cfbf3f2871f4c
- 7 exported PNGs (1080×1350): `/tmp/meta_ads_final/` (local, ephemeral)

## Tools used
- mcp__claude_ai_Meta__* (creative/tool audit)
- mcp__claude-design__*
- mcp__claude-in-chrome__* (screenshot, javascript_tool)
- mcp__claude_ai_Notion__*
- mcp__claude_ai_WordPress_com__* (attempted, rate-limited)
- Python/PIL, Bash
