# Session — 2026-07-19 (late evening) — galway-finance

## Objective
Follow up on the previous session's Meta rebuild: verify the 7 new ads cleared review, then work through budget/targeting/ad-count strategy for the two live campaigns.

## Summary
Confirmed all 7 rebuilt ads (cold V1–V5, retargeting V6–V7) are ACTIVE and cleared Meta review. Walked through several strategy questions with Callum: whether $15/day can hit his goals (no stated target exists — flagged the gap), why ad-level spend keeps shifting between creatives (Meta's delivery algorithm exploring under too little data — ~19 days needed to reach a stable 50-lead signal at current budget/historical CPL), local vs national targeting (recommended staying local — it's a core stated differentiator and national would dilute both positioning and the already-thin budget), and whether to cut ads or raise budget (recommended both, sequenced: budget now, ad-count cut once real data exists at the Jul 24–26 checkpoint). Callum proposed killing retargeting to fund a cold budget bump; pushed back — retargeting is cheap, protected from CBO starvation by design (settled Jul 13), and likely the account's best-economics channel, so cutting it without evidence would be a mistake. Landed on: bump cold to $20/day, keep retargeting untouched. Callum then explicitly authorized executing the change directly (overriding the standing recommend-only budget rule for this one instance) — dry-ran and applied it via the Meta Ads API, confirmed live.

## Outcomes
- Verified all 7 new ads (cold + RTG) are ACTIVE / cleared review
- Cold campaign (`120251478141370248`) daily budget increased **$15 → $20/day**, confirmed live via API (`updated_time` 2026-07-19T23:14:14+0800)
- Retargeting campaign (`120251478599460248`) left unchanged at $5/day
- Confirmed special ad category is still unset (`special_ad_categories: []`) on both campaigns — live-verified, not just recalled from memory

## Decisions
- **Cold budget → $20/day.** Reason: current $15/day spread across 5 ads reaches Meta's ~50-conversion learning-exit threshold in ~19 days at historical CPL — too slow to trust delivery data. $20/day shortens that meaningfully without committing to the $40–50/day needed for a textbook one-week exit.
- **Retargeting stays at $5/day, not cut.** Reason: warm audiences (site visitors 90d + FB engagers 365d) are structurally cheaper/higher-intent than cold, and the campaign was deliberately built as a separate ABO campaign on 2026-07-13 specifically to protect it from CBO budget starvation. No performance evidence yet justifies reversing that.
- **Targeting stays local (Alkimos 50km / Perth northern corridor), not national.** Reason: "local, in the corridor clients live in" is a stated core differentiator in `.agents/product-marketing.md`; content/compliance context (WA FHB grants, house-and-land) is regional; national would dilute both positioning and an already budget-thin delivery signal. Legally permitted (ACL 486112 isn't state-restricted) but not the right move at current stage/capacity.
- **Ad-count reduction (5→2-3 in the cold ad set) deferred to the Jul 24–26 checkpoint.** Reason: current per-ad data (11 total impressions) is noise, not signal — cutting now would be a guess, not a decision.
- **Agent executed a live budget change this session** on Callum's explicit in-session authorization, overriding the standing "agents recommend only" rule for this one instance. Standing rule itself is unchanged — this was a one-off, not a new default.

## Insights
- Meta's ad-level delivery reallocates spend across ads in an ad set in real time based on auction performance; with too little data per ad (~$3/day/ad here) this looks like noisy flip-flopping between "winners," not a real signal. Rule of thumb: want ~50 conversions per ad set within about a week to exit learning cleanly. (importance 4)
- Warm retargeting audiences are close to free insurance at $5/day and shouldn't be raided to fund cold budget increases — the marginal gain on cold is small (~$5/day) next to what's lost (the account's cheapest/highest-intent lead source). (importance 3)
- No stated CPL or lead-volume target exists anywhere in memory for the Meta campaigns — this is a real gap; strategy conversations keep hitting "I can't tell you if this is working without a number." (importance 4)

## Open loops
- **Jul 24–26 review** (new, consolidated checkpoint): judge Instant Form CPL with real data; cut cold ad set to top 2–3 performing ads; compare cold vs retargeting CPL; decide whether the $20/day bump is paying off or needs to go further. Owner: agent.
- Callum: set `FINANCIAL_PRODUCTS_SERVICES` special ad category on both campaigns (still unset, live-confirmed this session)
- Callum: fix Lead/CompleteRegistration pixel events on the site
- Callum: review Instant Form `2234033924078396` (questions, privacy link, completion message, notifications)
- Callum: define a target CPL or lead-volume goal for the Meta campaigns — strategy calls keep being made without one
- Week-2 blog post "Construction Loans in WA" — overdue, still not started
- Callum: publish FB organic post ("$100,000 apart")
- Carried: weekly-report idempotency confirm (Jul 20 run), meta-ad-review SKILL.md stale special-ad-category text, Purple Circle sign-off, privacy policy pixel check, product-marketing.md gaps, booked-exclusion audience still code 300

## Artifacts
- Campaign `120251478141370248` — daily_budget updated 1500→2000 (cents) via Meta Ads API

## Tools used
- startup, wrap-up skills; Pipeboard Meta Ads MCP (read + write: get_ads, get_campaign_details, get_adsets, bulk_get_insights, get_insights, update_campaign); Supabase MCP (read)
