# Session — 2026-07-25 (later) — galway-finance

## Objective
Confirm Pipeboard has been removed as a vendor and validate the replacement native Meta connector.

## Summary
Callum reported he stopped using Pipeboard and removed it as a vendor since Galway Finance now has direct Meta access. Verified the native `mcp__claude_ai_Meta__*` connector is live via `ads_get_ad_accounts` — ad account `1928354054506891` ("Galway Finance") is ACTIVE and queryable, with no third-party plan/execution cap. Updated local memory (`PREFERENCES.md`, `open-loops.md`, `projects/galway-finance.md`) and Supabase (`workstreams`, `insights`, `preferences`, `decisions`) to retire all Pipeboard references and record the native connector as the standing tool. This unblocks the previously-blocked "Meta ads optimization" workstream, clearing the way to push the drafted compliant ad-copy fix to disapproved ad `120251618482150248`.

## Outcomes
- Confirmed native Meta connector (`mcp__claude_ai_Meta__*`) live and queryable for ad account `1928354054506891`
- Updated local memory files to retire Pipeboard
- Updated Supabase workstreams/insights/preferences/decisions to reflect the connector switch
- Unblocked the "Meta ads optimization" workstream that was blocked on Pipeboard connectivity

## Decisions
- **Meta ads connector**: use the native `mcp__claude_ai_Meta__*` connector for all Meta ads work going forward. Pipeboard is fully decommissioned, not paused — Callum removed it as a vendor after gaining direct Meta access. Rationale: Pipeboard's weekly free-plan execution cap had blocked work twice (Jul 13, Jul 25); the native connector has no such cap.

## Insights
- The native Meta connector (`mcp__claude_ai_Meta__*`) supersedes Pipeboard entirely — any older session log or memory note referencing Pipeboard tool names is stale as of today.

## Open loops
- Push drafted compliant ad-copy fix to disapproved ad `120251618482150248` via native connector (`ads_create_creative` + `ads_update_entity`) — now unblocked, top priority
- RTG retargeting ad set `120251560809090248` still dark 5+ consecutive days — needs Ads Manager diagnostic
- Instant Form `2234033924078396` still missing `privacy_policy_url`
- `special_ad_category` still mismatched on both live campaigns (HOUSING/unset vs FINANCIAL_PRODUCTS_SERVICES)
- Week-2 blog post "Construction Loans in WA" still overdue since Jul 20

## Artifacts
- None created this session (memory/tooling update only)

## Tools used
- `mcp__claude_ai_Meta__ads_get_ad_accounts`, Supabase MCP, local memory files
