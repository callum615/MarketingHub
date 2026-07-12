# Session — 2026-07-12 — galway-finance

## Objective
Plan and build the Galway Finance marketing OS end-to-end (Phases 0–3), then consolidate the content pipeline into the existing Notion structure.

## Summary
Approved a 4-phase plan and executed all of it. Phase 0: repo cleanup, `.agents/product-marketing.md` created from live site copy + user answers, CRN mapping corrected (579221 = corporate, 579222 = Callum individual) across compliance file, Supabase, and context doc. Phase 1: built `meta-ad-review` + `meta-report` skills, verified on the live account — ad review found 6 fixes; report showed 7 leads Jul 8–9 (~A$5.60 CPL) then 3 zero-lead days with CPC → A$25.10. Phase 2: content strategy (5 pillars, 12-week calendar), `wp-publish` skill, week-1 post staged as WP draft 50. Phase 3: `weekly-marketing-report` skill, first report generated, cloud routine scheduled Mondays 8am Perth. Finally consolidated the editorial calendar into the existing Notion Content Library (Marketing Hub, Galway Finance Hub teamspace), migrated 12 posts, trashed the old DB, repointed skills + routine.

## Outcomes
- 4 custom skills shipped & verified: meta-ad-review, meta-report, wp-publish, weekly-marketing-report
- `.agents/product-marketing.md` + `.agents/content-strategy.md` (all skills read these)
- CRN mapping corrected everywhere: 579221 corporate / 579222 individual
- Week-1 post staged as WP draft (post 50, /resources/how-much-can-i-borrow/)
- 12-post blog pipeline in Notion Content Library (data source `40dcbf2b-102f-4efc-837e-86f426e6fe03`)
- First weekly report under Marketing Hub; routine `trig_01BvHrpCDxk9otssrUNMG34d` Mondays 8am Perth
- 8 commits pushed (through `ebfd64f`)

## Decisions
- **CRN usage**: 579221 on business-published content; 579222 only in Callum's personal name
- **OS scope**: Galway Finance only; Meta + WordPress first; phased automation
- **Single content DB**: Content Library is the sole pipeline (blog rows: Format=Blog, Channel=Website; Stage: Idea → Drafting → Editing [staged in WP] → Published); old calendar DB trashed

## Insights
- Meta lead ads convert on-platform — GA4 Paid Social sessions ≠ ad performance; judge leads in Meta
- Site core pages are block templates → WP API `pages.get` returns empty; fetch live URLs for copy. Blog posts ARE API-readable, live under /resources/
- Live campaign uses HOUSING special ad category; mortgage ads should likely be CREDIT (ad-review finding)
- Creative fatigue is fast here: CTR 1.0%→0.21% and CPC 6x within 3 days at A$25/day — plan weekly refreshes

## Open loops
- Publish the staged borrowing-power post (WP draft 50) — 2 min, Callum
- Mon/Tue: refresh ad creative if Jul 13 lead-less; bundle 6 ad-review fixes (CREDIT category, disclosure line, "best suits" wording, BOOK_TRAVEL CTA, image swap, headline whitespace)
- Add GA4 booking/lead key event (property 541904526)
- Purple Circle sign-off on AU-finance-compliance.md (Callum)
- Confirm "Test - New Homes Campaign" paused
- Check if routine's unexpected fire (Jul 12 08:53 UTC) made a duplicate report page
- Fill product-marketing.md gaps (metrics, verbatim customer language) as campaigns surface answers

## Artifacts
- Skills: `.claude/skills/{meta-ad-review,meta-report,wp-publish,weekly-marketing-report}/`
- Context: `.agents/product-marketing.md`, `.agents/content-strategy.md`
- WP draft: post 50 → https://galwayfinance.com.au/resources/how-much-can-i-borrow/
- Notion: Content Library (extended schema), "Marketing Week — Jul 6 to Jul 12" report, both under Marketing Hub
- Routine: trig_01BvHrpCDxk9otssrUNMG34d (manage: claude.ai/code/routines)

## Tools used
Supabase MCP · Pipeboard Meta Ads MCP · Pipeboard GA4 MCP · WordPress.com MCP · Notion MCP · RemoteTrigger · git/gh · skills: product-marketing, content-strategy, wp-publish, schedule
