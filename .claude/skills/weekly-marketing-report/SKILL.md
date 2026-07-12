---
name: weekly-marketing-report
description: Produce the weekly Galway Finance marketing report combining Meta Ads spend/leads and GA4 website traffic into one Notion page with plain-English commentary. Use when the user says "weekly report," "weekly marketing report," "marketing update," "how did marketing go this week," or when a scheduled routine triggers it. Read-only against all data sources; writes only the Notion report page.
---

# Weekly Marketing Report — Galway Finance

One page, one minute to read, one clear "do this next week." Combines paid (Meta) and site (GA4) into a single picture. Data pulls are read-only; the only write is the Notion report page.

## Data pulls

1. **Meta**: follow the `meta-report` skill's Step 1–2 (account `act_1928354054506891`, `last_7d` daily breakdown + prior-7d comparison, lead-counting and fatigue rules apply as written there).
2. **GA4** (property `541904526`, timezone Australia/Perth): `run_google_analytics_report` with two `dateRanges` (`7daysAgo→today` named `this_week`, `14daysAgo→8daysAgo` named `last_week`) — the comparison comes back in one call. Two pulls:
   - by `sessionDefaultChannelGroup`: sessions, activeUsers, keyEvents
   - by `pagePath` (this week only, ordered by screenPageViews, limit 10): what people actually read
3. Editorial calendar (Notion data source `703a45b1-1b1e-4698-90b2-b5aa97e09b54`): what shipped this week, what's queued next.

## Known measurement quirks (state them, don't hide them)

- **Meta lead ads convert on-platform** — GA4's "Paid Social" sessions will look tiny next to Meta spend. That's the funnel design, not a failure. Leads live in Meta's numbers.
- **GA4 has no booking/lead key event yet** (only purchase/qualify_lead/close_convert_lead) — until that's fixed, GA4 measures attention, not outcomes. Flag this gap in every report until it's closed.
- The account is young: small numbers, wide swings. Compare directionally, don't over-read percentages on bases under ~50.

## Report structure (create as a Notion page)

Title: `Marketing Week — [Mon D] to [Sun D Mon YYYY]`. Create via `notion-create-pages`. Parent: the "Marketing Reports" page if one exists (search first); otherwise create standalone and note where it landed.

```
TL;DR — 3 sentences max: money spent, leads in, the one action for next week.

## Paid (Meta)
Spend / leads (by type, per meta-report rules) / CPL / fatigue signals.
Table: this week vs last week.

## Website (GA4)
Sessions + users by channel, WoW. Top pages. Anything notable (a post ranking, a channel moving).

## Content
Shipped this week (from editorial calendar) · next week's queued post · pipeline health (any post stuck in Awaiting review > 7 days).

## Signals & risks
Fatigue flags, measurement gaps, compliance items awaiting sign-off.

## Next week
Max 3 actions, ordered by impact. Concrete, not "monitor performance."
```

## After creating the page

- Terminal output: just the TL;DR + the Notion page link.
- If any fatigue signal from `meta-report` is CRITICAL (e.g. 4+ days spend with zero leads), say so in the terminal output too — don't bury it in the page.

## Rules

- Read-only on Meta/GA4/WordPress. No campaign changes, no budget changes, regardless of what the data shows — recommend, don't act.
- Numbers must reconcile with their sources; if Meta and GA4 disagree, show both and explain why (usually the on-platform-leads quirk).
- No invented benchmarks — compare only against this account's own history.
