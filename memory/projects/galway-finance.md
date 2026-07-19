# Project — galway-finance

## 2026-07-19 (evening) — Full Meta audit; both campaigns rebuilt to Instant Form leads
Full 7-ad audit (compliance/creative/policy + performance + structure) resolved the zero-lead mystery: the website `Lead` pixel event died at the Jul 15 landing-page relaunch while both ad sets optimized toward it, AND every ad carried an Instant Form the optimization ignored — Meta had no valid signal either way. Worse, Meta's Advantage+ `text_optimizations` had auto-generated 6 non-compliant V5 copy variants ("best deal", disclosure line dropped) — a live compliance FAIL. Executed with Callum's approval: paused V5 → clean creative rebuild (single body, LEARN_MORE, `disable_all_enhancements`) → converted BOTH campaigns to Instant Form optimization via archive-old-ad-set + create-new (Meta locks attribution/optimization post-creation, and CBO requires one goal per campaign). New ad sets: cold `120251560593780248` (5 ads, A$15/day), RTG `120251560809090248` (2 clean ads, warm audiences, geo now Alkimos 50km per Callum, A$5/day). All 7 ads in Meta review as of session end; learning restarts from zero — judge after 5–7 days.

Key settled decisions:
- **Lead path = Instant Form** (form `2234033924078396`) on both campaigns — softer leads, database-building, calling practice; replaces website-conversion optimization entirely
- **Advantage+ enhancements always OFF** on regulated creatives (`disable_all_enhancements`) — text_optimizations produced non-compliant variants
- **Retargeting geo = Alkimos 50km** (matches broad campaign; geo only, warm audiences kept)

Gotchas learned: Meta locks `attribution_spec`/`optimization_goal` after ad-set creation (subcodes 1885560/1504040); lowest-cost CBO forces one optimization goal across ad sets (1885760) → archive old ad set first; LEAD_GENERATION requires 1d-click/0-view attribution; audit `asset_feed_spec` for hidden AI copy variants; event-based audiences stall when their source pixel event dies.

Still on Callum: special ad category (both campaigns, Ads Manager), pixel event fix (Events Manager/GTM), Instant Form question/notification review.

## 2026-07-18 (afternoon) — Weekly-report cron fixed, ad-hoc Meta check surfaces zero-lead streak
Root-caused the weekly-marketing-report "double-fire": the RemoteTrigger cron config (`trig_01BvHrpCDxk9otssrUNMG34d`, Monday 00:00 UTC = 8am Perth) was correct all along — the extra fires were Callum's own manual test runs via the trigger's `run` action, which log identically to real cron fires. Added an idempotency guard to `.claude/skills/weekly-marketing-report/SKILL.md` (checks Notion for the target week's page before touching Meta/GA4; exits immediately if found). Agreed Callum will use the `meta-report` skill ad-hoc (terminal-only, no Notion write) instead of firing the trigger manually going forward. Ran `meta-report` live and found a critical zero-lead streak: no leads or conversions of any kind for 5 days (~$119.66 spent) across the live serviceability duplicate campaigns.

Key settled decisions:
- **On-demand figures**: always use `meta-report` ad-hoc, never manually fire the weekly-marketing-report trigger
- **special_ad_category vs optimization_goal**: the former is a targeting/compliance restriction only; the latter (Instant Form / `LEAD_GENERATION`) is the likelier cause of zero tracked conversions — check Meta Events Manager for pixel firing as the concrete next diagnostic step

## 2026-07-13 (night) — Retargeting layer built (PAUSED, awaiting activation)
Full retargeting stack built for warm serviceability traffic: separate ABO campaign `META_Leads_RTG-Perth_Serviceability-LP_2026-07` (id `120251420896860248`, A$5/day, PAUSED), account's first 3 custom audiences (site visitors 90d `120251421421940248`, FB engagers 365d `120251420871500248`, booked-exclusion 180d `120251421422810248`), 2 new warm-angle circle-hybrid ads (V6 reminder, V7 next-step) in Meta review. Cold campaign day-1 was strong: CTR 3.8%, CPC A$1.02, 10 link clicks on A$24.40.

Key settled decisions:
- **Retargeting structure**: separate small ABO campaign, never an ad set inside the live CBO campaign (budget starvation); report warm CPL separately from cold CPL
- **Retargeting targeting hygiene**: always disable `targeting_relaxation_types` (Meta enables custom-audience expansion silently)
- **Warm audiences get dedicated creative** (reminder/objection angles), not recycled cold ads

Gotchas learned: WEBSITE custom audiences need the extra `web_custom_audience_tos` (only grantable via Ads Manager Create-Audience UI); Pipeboard free plan has a weekly command cap that blocks mid-workflow. Flag open: live campaign's special ad category reads empty via API — verify/fix.

## 2026-07-12 (night) — Serviceability campaign launched, replaced New Homes campaign
New Meta campaign live: `META_Leads_Broad-Perth_Serviceability-LP_2026-07` (id `120251395173300248`), A$20/day, ACTIVE, targeting the lender-serviceability angle for new-home buyers. Landing page published: `/new-home-borrowing-power/` (WP page 53). Old "New Homes Campaign" (A$25/day) paused. 5 ad variants built in a "circle hybrid" creative style (previous campaign's navy+circle-photo signature, modernized typography) — stored as reusable HTML/CSS cards in the Galway Finance Design System (`claude.ai/design`, project `63603262-f698-4cbb-88c9-9164ce140eb6`, "Ads" group), rendered via headless Chrome, not Canva.

Key settled decisions:
- **Special ad category**: use `FINANCIAL_PRODUCTS_SERVICES`, not `CREDIT` (Meta retired CREDIT)
- **Ad creative build tool**: Claude Design (HTML/CSS cards) preferred over Canva going forward — pixel-exact, brand-token-driven, reusable
- **Landing pages must be published (not draft) before ads referencing them go live** — Meta disapproves ads linking to unpublished drafts

## 2026-07-12 (evening) — GA4 key events + wrap-up git backup
GA4 property 541904526 now has `booking_cta_click` + `phone_click` as key events (ONCE_PER_SESSION) — closes the "no lead key event" gap at intent level; completed bookings still need a `generate_lead` tagging event. wrap-up skill now auto-commits + pushes `memory/` to origin at every session end.

## 2026-07-12 — Marketing OS built (Phases 0–3 complete)
Full stack now running: context docs (`.agents/product-marketing.md`, `.agents/content-strategy.md`) → 4 custom skills (meta-ad-review, meta-report, wp-publish, weekly-marketing-report) → Notion Content Library pipeline (12 posts queued, weekly cadence) → scheduled Monday 8am Perth report routine (`trig_01BvHrpCDxk9otssrUNMG34d`). Week-1 post staged as WP draft 50.

Key settled decisions:
- **CRN**: 579221 (corporate) on business content; 579222 (Callum individual) personal-name only
- **Scope**: Galway Finance only; Meta ads + WordPress/SEO first; phased automation, human publishes everything
- **Notion**: Content Library on Marketing Hub (Galway Finance Hub teamspace) is the single content DB — data source `40dcbf2b-102f-4efc-837e-86f426e6fe03`, blog rows Format=Blog, Stage: Idea → Drafting → Editing (staged in WP) → Published

Key IDs: Meta account `act_1928354054506891` · GA4 property `541904526` · WP site galwayfinance.com.au (blog_id 254908544, posts under /resources/) · Marketing Hub page `0bf905a3-5213-406f-a226-34926b1d145a`

## 2026-07-11 — Foundation
Memory system (Supabase + startup/wrap-up), 37 marketing skills installed + pruned, AU-finance-compliance.md guardrails wired into regulated skills.
