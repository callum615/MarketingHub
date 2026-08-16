# Session — 2026-07-26 — galway-finance

## Objective
Continue the in-person referral-network workstream: check tracker status and produce the agent-owned deliverables (partner one-pager, one-liner).

## Summary
Startup surfaced that this git worktree's local `memory/` files were stale (last commit 2026-07-21) while Supabase — and a separate branch, `emerald-range` — had 5 more wrap-up sessions through 2026-07-25 that never made it into this worktree/branch. Flagged to Callum; treated Supabase as authoritative for the brief. Callum then said to focus only on in-person marketing this session.

Pulled the live Notion "Referral Network Plan — Progress" tracker: all 12 tasks still "Not Started," several overdue (contact list Jul 22, one-liner Jul 23, Purple Circle confirmation Jul 23, prospect list Jul 25, partner one-pager Jul 25). Drafted the two agent-owned deliverables — a "what's in it for you" one-liner and a full partner one-pager — initially framed as pure reciprocity (no fees), consistent with the existing compliance guardrail file's blanket "referral fees tied to loan value/volume are prohibited" language. Published as a new Notion page under Marketing Hub, linked from it, and moved two tracker tasks to "In Progress."

Callum then corrected the framing: referral partners will be paid via a **commission-split structure under Purple Circle's own referral agreement template**, not pure reciprocity. Updated `.claude/AU-finance-compliance.md` to document aggregator-templated commission-split arrangements as the accepted compliant mechanism (the old blanket "likely prohibited" line was too broad — it's DIY/non-templated fee structures that need compliance review, not the aggregator's own vetted template). Rewrote the Notion one-pager and one-liner to pitch a formal paid partnership, deliberately omitting the specific split percentage since that's a contract term for the signed agreement, not marketing copy.

## Outcomes
- Notion page created: "Referral Partner One-Pager (DRAFT — pending Purple Circle sign-off)" under Marketing Hub — https://app.notion.com/p/3a9c844e9c4381119e22f7784ced6826
- `.claude/AU-finance-compliance.md` updated — commission-split referral arrangements under an aggregator's own template documented as the accepted compliant mechanism
- Notion tracker: "Draft the one-liner" and "Create the partner one-pager" tasks moved Not Started → In Progress, with notes

## Decisions
- **Referral partner commission structure**: commission split (share of Callum's lender-paid commission, paid on settlement) under Purple Circle's own referral agreement template — not pure reciprocity. Purple Circle holds the ACL and vets its own template, so this aggregator-provided mechanism is treated as compliant with the conflicted-remuneration ban; custom/non-templated structures still need explicit compliance review.
- **Referral collateral omits commission percentages** — described as "a formal referral partnership" / "commission split," with the actual split % left to the signed agreement, not marketing copy.

## Insights
- This worktree (`branched-badger`) is behind: local `memory/` stops at 2026-07-21, but 5 more wrap-up commits exist through 2026-07-25 only on branch `emerald-range`. Supabase stayed current throughout — treat it as authoritative when a worktree's local files look stale, and reconcile branches when convenient.
- The conflicted-remuneration ban targets volume/value-tied and improvised commission structures, not all referral commissions — an aggregator's own vetted template (like Purple Circle's) is the accepted compliant mechanism since the aggregator holds the ACL.

## Open loops
- Get the Purple Circle referral agreement paperwork ready/in hand — Callum
- Review and approve the one-liner/one-pager copy — Callum
- List and rank existing loose contacts by type/warmth — Callum, overdue since Jul 22
- Build target prospect list (5–8 per type, Perth metro) — Callum, overdue since Jul 25
- Reconcile this worktree's local memory/ with the newer commits on branch `emerald-range` — low priority hygiene

## Artifacts
- https://app.notion.com/p/3a9c844e9c4381119e22f7784ced6826 (Referral Partner One-Pager, DRAFT)
- `.claude/AU-finance-compliance.md` (edited, not a memory/ path — not auto-committed, see receipt)

## Tools used
- Notion MCP, Supabase MCP, local file edit
