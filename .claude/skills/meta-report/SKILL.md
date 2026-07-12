---
name: meta-report
description: Pull Meta Ads performance for Galway Finance and produce a plain-English report with spend, leads, cost-per-lead, and fatigue signals. Use when the user says "meta report," "ad performance," "how are my ads doing," "ad spend report," "weekly ad report," or asks about leads/CPL/results from Facebook or Instagram ads. Read-only; also the template for the scheduled weekly report.
---

# Meta Ads Performance Report — Galway Finance

Produce a report a busy broker can act on in 60 seconds. Numbers second, meaning first. Read-only against the ad account.

Account: `act_1928354054506891` ("Galway Finance"), currency AUD. (Personal account `act_659431211572135` exists — ignore unless asked.)

## Step 1 — Pull data

1. `get_insights(object_id=act_1928354054506891, level="campaign", time_range="last_7d", time_breakdown="day")` — the core pull.
2. For week-over-week: a second call with `{since, until}` for the prior 7 days. Skip if the account is too young to have a prior week.
3. If a campaign looks broken or fatigued, drill to `level="ad"` for that campaign before recommending anything.

## Step 2 — Interpret (know the data quirks)

**Lead counting — do not blindly sum action types.** The same lead fires multiple action types. Report two separate lead numbers:
- **Meta instant-form leads**: `lead` / `onsite_conversion.lead_grouped`
- **Website conversions** (booking-page pixel): `complete_registration` / `offsite_conversion.fb_pixel_complete_registration`

These can overlap conceptually but track different funnels. CPL = spend ÷ (the lead figure relevant to that campaign's objective); state which definition was used.

**Fatigue / decay signals** (flag when present, with the numbers):
- CTR trending down across the window (compare first half vs second half of the daily breakdown)
- CPC rising day over day
- Frequency > 2.0 (audience saturation; > 1.5 and climbing on a small audience is an early warning)
- Days since last lead while spend continues — the loudest signal; call it out explicitly

**Hygiene checks while in there:**
- Test/duplicate campaigns still spending (anything named "Test …")
- Campaigns spending with zero results for 3+ days

## Step 3 — Output format

```
# Meta Ads Report — [date range]

**TL;DR:** [2-3 sentences: what happened, the one thing to do about it]

## Numbers
| Metric | This week | Last week | Change |
(spend, impressions, reach, clicks, CTR, CPC, leads by type, CPL)

## By campaign
[one row per campaign that spent]

## Signals
[fatigue/decay/hygiene findings, each with its evidence]

## Recommended actions
[max 3, ordered by impact; each one concrete enough to do today]
```

Omit the "Last week" column when there's no prior period. Round currency to cents, percentages to 2dp.

## Rules

- Never present engagement actions (post_engagement, page_engagement) as results — they're noise for a lead-gen account.
- A recommendation to pause/kill an ad needs at least 5–7 days of data or clear spend-with-zero-results; note sample size when data is thin (this account is new — say so rather than over-reading small numbers).
- Read-only: no pausing, budget changes, or edits. If the user asks for a change, confirm the exact change first.
- When run as a scheduled routine, write the report to Notion (human-facing docs live there) and keep the terminal output to the TL;DR.
