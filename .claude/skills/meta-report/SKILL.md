---
name: meta-report
description: Pull Meta Ads performance for Galway Finance and produce a plain-English report with spend, leads, cost-per-lead, and fatigue signals. Use when the user says "meta report," "ad performance," "how are my ads doing," "ad spend report," "weekly ad report," or asks about leads/CPL/results from Facebook or Instagram ads. Read-only; also the template for the scheduled weekly report.
---

# Meta Ads Performance Report — Galway Finance

Produce a report a busy broker can act on in 60 seconds. Numbers second, meaning first. Read-only against the ad account.

Account: `1928354054506891` ("Galway Finance"), currency AUD. (Personal account `659431211572135` exists — ignore unless asked.) Note: the native Meta connector (`mcp__claude_ai_Meta__*`) takes the bare numeric account ID, not the legacy `act_`-prefixed form used by the old Graph API / Pipeboard tooling.

## Step 1 — Pull data

Use the native Meta connector's `ads_get_ad_entities` tool (Pipeboard and its `get_insights` tool were decommissioned 2026-07-25 — do not reference that tool name, it no longer exists).

1. Core pull: `ads_get_ad_entities(ad_account_id="1928354054506891", level="campaign", date_preset="last_7d", time_increment="1", fields=["name","amount_spent","impressions","reach","clicks","ctr","cpc","frequency","lead","onsite_conversion_lead_grouped","omni_complete_registration","cost_per_lead","results","cost_per_result"])` — daily breakdown for the trailing 7 days. Field names verified live 2026-08-09; `spend`/`actions`/`campaign_name` (used by the old Pipeboard tool) are NOT valid here — use `amount_spent`/`name` and the named conversion fields above instead of a generic `actions` array. A campaign/ad set with zero delivery in the window returns no metric fields at all (not zero values) — that's expected, not an error.
2. For week-over-week: a second call with `time_range='{"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}'` for the prior 7 days (omit `time_increment` for a single aggregate row). Skip if the account is too young to have a prior week.
3. If a campaign looks broken or fatigued, drill to `level="ad"` for that campaign before recommending anything.
4. If any field name in the call above errors, the error message lists all currently-supported fields for that level — read it and retry with valid names rather than guessing repeatedly.

## Step 2 — Interpret (know the data quirks)

**Lead counting — do not blindly sum action types.** The same lead fires multiple fields. Report two separate lead numbers, pulled directly (not summed from an `actions` array — that field isn't queryable at campaign/ad level here):
- **Meta instant-form leads**: the `lead` field (falls back to `onsite_conversion_lead_grouped` if `lead` is absent for a campaign)
- **Website conversions** (booking-page pixel): `omni_complete_registration`

These can overlap conceptually but track different funnels. CPL = spend ÷ (the lead figure relevant to that campaign's objective) — use `cost_per_lead` directly when Meta reports it, otherwise compute `amount_spent ÷ lead`; state which definition was used.

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
