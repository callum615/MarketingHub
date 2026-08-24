# Session — 2026-08-24 — galway-finance

## Objective
Run `/startup` to restore context and establish what state the work is actually in.

## Summary
Startup-only session; no marketing work executed. Loaded Supabase memory (authoritative, current through 2026-08-24) alongside this worktree's local `memory/` files, which stop at 2026-07-27 — confirming `branched-badger` is ~4 weeks stale and should not be treated as a source of truth.

The substantive finding: `.claude/AU-finance-compliance.md` carries an **uncommitted** change in this worktree containing the "Settled 2026-07-26" paragraph legitimising **commission-split referral fees under Purple Circle's own agreement template** (replacing the older blanket "referral fees likely prohibited" framing). Verified via `git show origin/main` that main does **not** contain this paragraph.

This contradicts the 2026-08-16 cleanup session's conclusion that the compliance file was byte-identical across all branches and nothing was lost — that check compared committed trees and missed uncommitted working-tree changes. The paragraph is a live guardrail governing the currently-active referral partner workstream, so losing it would be material.

## Outcomes
- Session Brief covering: Meta ads blocked on funding (~$500+ spent since Jul 12, zero leads ever, CPC $2.84→$8.51); referral partner network as the active front (3 real outreach emails sent 2026-08-17, A&T draft unsent); self-employed ICP repositioning; content backlog of 4 posts 14–35 days overdue.
- Confirmed local memory here is stale vs Supabase; Supabase treated as authoritative.
- Identified branch-unique, uncommitted compliance guardrail text absent from `origin/main`.

## Decisions
- None settled this session.

## Insights
- The 2026-08-16 drift audit's "byte-identical, nothing lost" conclusion was wrong — it compared committed trees only. **Future drift audits must run `git status` / `git diff` in each worktree**, not just diff committed content.
- Guardrail edits to `.claude/AU-finance-compliance.md` are non-memory files, so the standing "commit `memory/` only" rule leaves them uncommitted indefinitely. A compliance guardrail change must be flagged explicitly for commit at wrap-up, not just mentioned in the receipt.

## Open loops
- **Commit `.claude/AU-finance-compliance.md` to main** — the "Settled 2026-07-26" Purple Circle commission-split paragraph is the only copy of a settled compliance guardrail and lives only in this worktree's uncommitted working tree. Owner: agent, on Callum's explicit go-ahead (non-memory file).
- Prefer working from `main` rather than this worktree going forward.

## Artifacts
- None created.

## Tools used
- `startup` skill, `load_context.py` (Supabase), git, bash
