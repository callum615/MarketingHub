# Project — galway-finance

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
