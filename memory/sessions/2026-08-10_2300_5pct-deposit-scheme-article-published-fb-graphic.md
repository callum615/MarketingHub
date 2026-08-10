# Session — 2026-08-10 — galway-finance

## Objective
Publish a blog article on the Australian Government's 5% Deposit Scheme and create a Facebook promotional graphic linking to it.

## Summary
Continued from the meta-report fix session: confirmed the Meta campaign pause was a budget issue (not technical) and committed the weekly-report fix (52fcfb3, still unpushed). Researched, planned, drafted, and staged a new blog article on the 5% Deposit Scheme (WA-focused, kept standalone from the queued Grants & Schemes hub post), sourced two Pexels images, fixed a duplicate-hero-image bug, and published it live at Callum's explicit confirmation. Iterated the copy per feedback (removed em-dashes, added a "what happens if you move out" FAQ) and logged it in the Notion Content Library as Published. Built a matching Facebook link-post graphic in Claude Design using the existing brand ad-template system, iterating through several headline options before landing on a question-led final headline.

## Outcomes
- Published blog post: The 5% Deposit Scheme in WA (https://galwayfinance.com.au/resources/5-percent-deposit-scheme-wa/, WP post 69)
- Notion Content Library row created and marked Published for the new article
- Facebook link-post graphic built in Claude Design (Social media ad templates project) at 1200×628, using the article's hero photo
- Committed weekly-marketing-report/meta-report Pipeboard→native-connector fix (commit `52fcfb3`) — still unpushed to origin

## Decisions
- **Meta campaign pause root cause**: confirmed as running out of budget, not technical or deliberate strategy. Reactivation is Callum's funding call, not a diagnostic task.
- **5% Deposit Scheme article scope**: standalone deep-dive, kept separate from the queued broader "First Home Buyer Grants & Schemes in WA" hub post (which will link to this piece once written).
- **This article's CTA**: set to `/contact/` instead of the site's usual default `/booking/`, per Callum's explicit direction for this one piece — not a change to the standing default CTA.
- **Blog copy style**: reduce/avoid em-dashes in long-form blog articles going forward (rewrite as commas, periods, colons, parentheses) to avoid reading as AI-generated. Note: the brand design system's own copy guide lists em-dash as on-brand for ad/social copy — this preference is specific to long-form blog content, not ad/social creative.

## Insights
- Base64-encoding images for WordPress/Claude Design MCP write calls is extremely token-expensive (~1 token per base64 character — a 40KB image cost 50k+ tokens just to read back). Use browser-based `file_upload` (Chrome extension, disk-path based, zero context cost) against the target app's own upload UI instead of the MCP tool's base64 parameter, for any real image.
- Stock photos can carry baked-in text/graphics irrelevant or wrong for the context (a Pexels "keys" photo had embedded US-specific promotional copy referencing the Federal Reserve and COVID). Always verify a candidate stock image's actual visual content via WebFetch description before downloading and using it — the search snippet alone isn't enough.
- `wp-publish`'s "agents never auto-publish, even if asked casually" rule held up even for a direct question like "can you publish it?" — treated it as a question requiring an explicit yes rather than itself being the confirmation, and it worked cleanly.
- For any new Meta/social ad-style graphic, reuse the "Social media ad templates" Claude Design project (`e5106aea-b312-446d-b2b9-49175d1de155`) and its bound Galway Finance Design System rather than starting fresh — it already has the brand palette, fonts, logos, and an established "split link" 1200×628 pattern ideal for link-out posts. The `image-slot` component's `src`/`credit` attributes can point directly at an already-hosted image URL (e.g. a WordPress media library file) with no re-upload needed.

## Open loops
- Push commit `52fcfb3` to origin (weekly-marketing-report fix) — local only as of session end.
- Overdue Week-2 blog post: "Construction Loans in WA: How Progress Payments Actually Work" — still not started (~3 weeks overdue).
- Broader "First Home Buyer Grants & Schemes in WA" hub post still queued (~2 weeks overdue) — should link to the new 5% Deposit Scheme article once written.
- AdvisorPPC (Google Ads/GA4 connector) setup still parked pending Callum resolving a connection issue.
- Facebook graphic ready but not yet posted — Callum to publish to Facebook himself (no Facebook posting capability in this environment).
- Consider building square 1:1 / Stories 9:16 versions of the FB graphic if reused across other channels — not requested yet.

## Artifacts
- Blog post: https://galwayfinance.com.au/resources/5-percent-deposit-scheme-wa/ (WP post 69)
- Notion Content Library row: https://www.notion.so/3b8c844e9c43813ab359f720c627b2de (Stage: Published)
- Claude Design file: "FB Post - 5pct Deposit Scheme.dc.html" in project `e5106aea-b312-446d-b2b9-49175d1de155`
- Git commit `52fcfb3` on `emerald-range` (weekly-marketing-report Meta pull fix) — unpushed

## Tools used
- wpcom-mcp-content-authoring (WordPress), Notion MCP, WebSearch, WebFetch, claude-in-chrome (file_upload, screenshots, console), Claude Design MCP, Supabase MCP
