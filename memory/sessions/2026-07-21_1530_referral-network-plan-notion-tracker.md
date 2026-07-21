# Session — 2026-07-21 — galway-finance

## Objective
Build a plan and Notion-based progress tracker for launching Galway Finance's in-person referral network with accountants, financial planners, and building reps.

## Summary
In plan mode, designed a phased referral-network strategy (compliance check → foundation → outreach → relationship-building → review) for building professional referral relationships across wider Perth metro, governed by the AU conflicted-remuneration ban (no fees tied to loan value/volume to referrers). Research confirmed neither the existing `referrals` skill (customer/affiliate loops) nor `co-marketing` skill (SaaS partnerships) cleanly fits professional in-person partner-building. After plan approval, built a "Referral Network Plan — Progress" database inside the existing Notion Marketing Hub. The user explicitly redirected away from an initial partner-CRM design toward a pure plan/task-progress tracker, so the database was rebuilt around 12 tasks across the 5 phases (Task/Phase/Status/Owner/Due Date/Notes). Fixed a Notion embedding quirk along the way — a newly created database defaulted to `is_inline=false` and got bumped to a stray top-of-page link instead of embedding under its heading; fixed via `is_inline` update plus a full `replace_content` pass. All 12 tasks were then assigned due dates from Jul 22 to Aug 21, 2026, paced to the user's stated 3-5 hrs/week capacity.

## Outcomes
- Referral network plan written and approved (5 phases, compliance-first model)
- Notion "Referral Network Plan — Progress" database created inside Marketing Hub with 12 tasks
- All 12 tasks assigned due dates Jul 22 - Aug 21, 2026
- Plan file saved at `~/.claude/plans/i-am-wanting-to-compressed-pancake.md`

## Decisions
- **Referral-network compensation model**: no fees tied to loan value/volume to accountants, planners, or builders — reciprocal referrals + shared value only. Purple Circle sign-off on the exact structure is still open, not yet confirmed.
- **Geography**: wider Perth metro, not restricted to the Alkimos/northern-corridor campaign geography.
- **Time budget**: 3-5 hrs/week for in-person relationship-building.
- **Notion tracker scope**: plan/task progress only (Task/Phase/Status/Owner/Due Date/Notes) — explicitly not a partner-level CRM. User corrected the initial CRM build mid-session.

## Insights
- Neither `referrals` nor `co-marketing` skill cleanly fits an in-person professional referral network; borrowed compliance framing from `referrals` and partner-identification logic from `co-marketing`.
- Notion gotcha: new databases default `is_inline=false`; embedding via `update_content` search-replace can misplace the block (bumped to a stray link at page top). Fix: `notion-update-data-source` with `is_inline: true`, then `replace_content` with the full corrected page body rather than a partial search-replace.
- Building reps (display village / new-home sales consultants) are likely the highest-leverage, most time-sensitive partner type — finance pre-approval urgency before contract signing creates natural high-intent referrals.

## Open loops
- Jul 22: List and rank existing loose contacts by type/warmth
- Jul 23: Confirm referral-relationship structure with Purple Circle (reciprocal only, no fees tied to loan value/volume)
- Jul 23: Draft the standard "what's in it for you" one-liner for partners
- Jul 25: Build target prospect list (5-8 per type) across Perth metro
- Jul 25: Create the partner one-pager (reuse product-marketing differentiators)
- Jul 28: Re-engage existing loose contacts (reconnect + coffee ask)
- Aug 1: Scope a local networking group (BNI/chamber) as a force-multiplier
- Aug 4: Begin warm-intro/cold outreach to new targets
- Aug 11: Give-first referrals to new partners
- Aug 18: Set recurring touch cadence per active partner
- Aug 21: Monthly review of referrals in/out and conversion by partner type
- Aug 21: Fold this workstream into `memory/projects/galway-finance.md` and `open-loops.md` as its own ongoing entry

## Artifacts
- Notion database: "Referral Network Plan — Progress" (Marketing Hub) — https://app.notion.com/p/7c7b7798253648499755c3bdad36e85e
- Plan file: `/Users/callumduffy/.claude/plans/i-am-wanting-to-compressed-pancake.md`

## Tools used
Notion MCP (fetch, create-database, update-data-source, create-pages, update-page), Agent (Explore/general-purpose research), AskUserQuestion, Plan mode, Supabase (`save_context.py`).
