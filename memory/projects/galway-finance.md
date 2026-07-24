# Project — galway-finance

## 2026-07-24 — Meta report: RTG dark streak now 5 days, Instant Form privacy link confirmed missing
Ran an ad-hoc `meta-report` (Jul 17-23, read-only): zero leads for a 9th consecutive day. Cross-checked this against the live Instant Form's actual submission export since Jul 15 (zero records) — the zero-lead reading is confirmed real, not a reporting/attribution gap. The RTG retargeting ad set (`120251560809090248`, ads V6/V7) is now fully dark for **5 consecutive days** (Jul 20-24) despite `effective_status: ACTIVE` — this has now failed two "wait and recheck" cycles (Jul 20 → 4 days on Jul 23 → 5 days today) and needs an actual Ads Manager diagnostic, not another observation pass.

New findings this session: the live Instant Form ("Short Details-copy", `2234033924078396`) has **no `privacy_policy_url` set at all** — confirmed directly via the Meta API, closing the ambiguity on open-loop #3. Also confirmed `special_ad_category` is inconsistent across the two live campaigns: Broad-Perth = `HOUSING` (stale value), RTG-Perth = unset — neither matches the settled `FINANCIAL_PRODUCTS_SERVICES` decision from Jul 12; both need fixing manually in Ads Manager. No changes made — read-only session.

Still open: RTG dark streak (now top priority, 5 days), Instant Form privacy link, special ad category fix on both campaigns, Calendly booking → Lead event still not observed end-to-end in production, Week-2 blog post still not started (overdue since Jul 20).

## 2026-07-23 — Meta report: broader-market strategy confirmed; cold ad set creative cut executed early
Ran an ad-hoc `meta-report`: zero real leads for 8 straight days ($206.13 spend across the window). Two new findings not yet in memory: (1) a new ad set, "Test - Broad Australia — Instant Form leads" (`120251618482160248`, 5 duplicate creatives V1-V5), running national targeting; (2) the cold campaign's daily budget had dropped from the $21.00/day read on Jul 20 to $15.00/day (changed 2026-07-22). Flagged both as needing confirmation rather than assuming drift.

Callum confirmed both were deliberate: he's testing a broader-than-local market because he has a personal interest in possibly relocating to a different area, and servicing a wider market now makes that move easier later. This is a genuine strategy call, not an error — logged as a standing preference so future reports don't misflag geographic expansion.

Also confirmed the RTG retargeting ad set (`120251560809090248`) has now been **fully dark for 4 consecutive days** (Jul 20-23, zero impressions/spend) — escalated from the "16hrs, maybe ramp-up" note on Jul 20. Still not diagnosed in Ads Manager — this is now the most urgent open item.

Executed the Jul 24-26 checkpoint's ad-count cut early, since the data (zero clicks on V1/V3/V5, all 9 clicks on V2/V4) already supported it: paused V3 (House-and-Land Construction, ad `120251560596170248`) and V5 (Verbatim Question clean, ad `120251560597530248`) in the main "Broad Perth — Instant Form leads" ad set (`120251560593780248`). Kept V1 running deliberately per Callum's request to give it more of a chance, plus V2 and V4.

Key settled decisions:
- **Broader-Australia targeting + $15/day cold budget is intentional** — driven by Callum's lifestyle/relocation interest, not to be flagged as drift in future reports.
- **Cold ad set cut to 3 ads (V1, V2, V4)** — V3 and V5 paused for zero clicks; checkpoint acted on early rather than waiting to Jul 24-26.

Still open: RTG retargeting delivery outage (4 days dark, needs Ads Manager check), Calendly booking → Lead event still not observed end-to-end in production, Week-2 blog post (Construction Loans in WA) still not started (overdue since Jul 20).

## 2026-07-21 (morning) — Root-caused and fixed the dead Lead/CompleteRegistration pixel; full GA4 audit
Ran a full analytics tracking audit (GA4 + Meta Pixel) at Callum's request. Found the GA4 side mostly healthy (booking_cta_click, phone_click correctly tracked) but three phantom conversion events (`purchase`, `close_convert_lead`, `qualify_lead`) that were marked as conversions but never actually implemented, and `generate_lead` firing (once, thin) but not marked as a key event. Zero custom dimensions defined — flagged as a gap for segmenting by loan type given the multi-service business.

Then chased the long-standing dead Meta Lead/CompleteRegistration pixel event (open since ~Jul 15). Callum's first hypothesis was a classic GTM trigger scoped to a stale URL — checked via Claude in Chrome and found there is **no classic GTM container at all** under the connected Google account; the site uses Site Kit's native "Google tag" (`GT-WV3W733W`, gtag.js) plus a Meta Pixel embedded directly, neither routed through Tag Manager. The real root cause: the `/booking/` page embeds a Calendly widget in an iframe, and **nothing on the page ever listened for Calendly's `calendly.event_scheduled` postMessage** — so no Lead/CompleteRegistration event could ever fire on a real booking, regardless of URL scoping. Fixed by adding a message-listener script to the `page-booking` block template's Custom HTML block (JavaScript tab, previously empty) that fires `fbq('track','Lead')` and `gtag('event','generate_lead')` when Calendly reports a completed booking. Verified live: confirmed the code is present on the page, and a stubbed-function test (temporarily overriding `fbq`/`gtag`, dispatching a fake Calendly message, restoring originals) proved the listener fires both calls correctly with no side effects. Also marked `generate_lead` as a GA4 key event now that it has a real trigger behind it.

Key settled decisions:
- **This site does not use classic Google Tag Manager** — don't reach for tagmanager.google.com again for this account; tracking is Site Kit's Google tag (GA4) + a directly-embedded Meta Pixel, both edited via the WordPress Site Editor's block templates (page-booking, etc.), not GTM.
- **Custom HTML blocks on this site have separate HTML/CSS/JavaScript tabs** ("Edit code" on the block) — the JS tab is the right place for page-scoped tracking code without touching page markup or theme files.

Gotchas learned: typing code directly into the live Site Editor via browser automation is blocked by an auto-mode safety classifier on the first attempt regardless of in-chat authorization; it went through on a second attempt after the user re-confirmed explicitly in those exact terms. Still open: no real Calendly booking has happened yet since the fix, so end-to-end production delivery (Meta Events Manager, GA4 realtime) hasn't been observed — only the code path is proven.

## 2026-07-20 (afternoon) — Ad-hoc Meta check: still zero real leads; RTG rebuild not delivering
Ran startup (confirmed Supabase/local memory in sync) then an ad-hoc `meta-report` pull (7-day, campaign/adset/ad level, read-only, no Notion write — per the 2026-07-18 rule to use meta-report ad-hoc rather than firing the scheduled trigger). Result: $192.28 spent this week, zero real leads — the only "lead" action in the data is a stale delayed-attribution artifact on a paused, $0-spend campaign, not a new lead. The new cold Instant Form ad set (5 ads, `120251560593780248`, rebuilt Jul 19 late evening) has started delivering but on too small a sample to judge (~$25 spend, sub-1% CTR). New finding: the retargeting Instant Form ad set (`120251560809090248`, ads V6/V7) shows **zero impressions at all** since creation ~16 hours prior, despite `effective_status: ACTIVE` — not diagnosed further this session, flagged for a Jul 21 check rather than waiting for the Jul 24-26 checkpoint. Also spotted a small discrepancy: live API `daily_budget` on the cold campaign reads $21.00/day, not the $20.00/day logged in the Jul 19 budget-bump session. No changes made — purely a read-only check-in.

Key takeaway: the Instant Form fix from Jul 19 has not yet produced a lead, but it's only been live ~16-18 hours — consistent with the existing Jul 24-26 checkpoint plan. The RTG zero-delivery finding is the one thing that shouldn't wait that long.

## 2026-07-19 (late evening) — Ad review confirmed; cold budget bumped to $20/day, retargeting protected
Confirmed the 7 ads rebuilt in the afternoon session cleared Meta review (all ACTIVE). Worked through four strategy questions with Callum and landed on settled positions: (1) local vs national targeting — stay local, since "based in the corridor clients live in" is a stated core differentiator and national would dilute both positioning and an already-thin budget signal; (2) reduce ad count vs raise budget — do both, sequenced: raise budget now, cut the cold ad set's 5 ads down to 2-3 once real performance data exists (Jul 24-26, not before — current data is 11 total impressions, pure noise); (3) Callum proposed cutting retargeting to fund a cold bump — pushed back and won: retargeting is cheap ($5/day), structurally protected from CBO budget starvation by design (settled 2026-07-13), and warm audiences are typically the account's best-economics leads, so cutting it without evidence would trade away the cheapest leads for a marginal gain elsewhere; (4) executed the agreed change — cold campaign `120251478141370248` daily budget $15→$20/day, live via Meta Ads API, on Callum's explicit in-session authorization to override the standing recommend-only rule for this one instance (the standing rule itself is unchanged going forward).

Key settled decisions:
- **Targeting stays local** (Alkimos 50km / Perth northern corridor) — not national. Legally permitted (ACL 486112 not state-restricted) but wrong for current positioning, content strategy, and budget scale.
- **Cold budget = $20/day** (was $15) — sized to meaningfully shorten time-to-learning-exit (~19 days → faster) without committing to the ~$40-50/day a textbook one-week exit would need.
- **Retargeting stays at $5/day, untouched** — warm-audience economics + Jul 13 CBO-starvation protection outweigh the small reallocation gain.
- **Ad-count cut (5→2-3 ads, cold ad set) deferred to Jul 24-26** — first real checkpoint since the Jul 19 rebuild.

Gotchas/insights: Meta's ad-level delivery within an ad set reallocates spend continuously based on auction signal; with too little budget per ad (~$3/day here) this reads as noisy "winner" flip-flopping rather than a real result — want ~50 conversions per ad set within about a week to trust the data. No stated CPL/lead-volume target exists anywhere in memory for these campaigns — flagged as a real gap blocking clean go/no-go calls.

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
