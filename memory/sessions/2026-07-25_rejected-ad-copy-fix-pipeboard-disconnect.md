# Session — 2026-07-25 — galway-finance

## Objective
Push the compliance-fixed ad copy to the disapproved ad (V1 Two Lenders hero, Test-Broad-Australia ad set) and resolve why it was rejected.

## Summary
Traced the DISAPPROVED ad flagged in the Jul 24 report to ad `120251618482150248` ("V1 Two Lenders (hero)", Test-Broad-Australia ad set, campaign `120251478141370248`). Meta's activity log shows it flipped Active → Not approved on Jul 22 17:20, while its 4 sibling ads in the same duplicated ad set cleared review fine. Root-caused via the creative body text: it contained "no credit check from an enquiry" — a known trigger phrase under Meta's financial-services/credit ad policy — and the creative also had `text_optimizations` OPT_IN, inconsistent with the account's Jul 19 standing rule (Advantage+ enhancements always OFF on regulated creatives). Drafted a compliant rewrite: removed the "no credit check" claim entirely and fixed a hyper-local claim ("Perth northern-suburbs brokerage based in Eglinton") that was inconsistent with this ad set's national test targeting.

Attempted to push the fix via Pipeboard Meta Ads (create a new creative with `disable_all_enhancements=true`, then swap it onto the ad) but hit Pipeboard's weekly free-plan AI tool execution cap on the very first (dry-run) call. User then relinked something, but the Pipeboard Meta Ads MCP came back as **fully disconnected** rather than reconnected — confirmed there is no separate native Meta Graph API connector in this environment; Pipeboard is the only bridge. The copy fix was never pushed to Meta this session. Ending session to start fresh with a newly connected MCP.

## Outcomes
- Root-caused the ad disapproval to a "no credit check" policy-risk phrase plus `text_optimizations` left OPT_IN
- Drafted compliant replacement ad copy for ad `120251618482150248` — ready to apply, not yet pushed to Meta
- Confirmed no native/direct Meta Graph API MCP exists separate from Pipeboard in this environment
- Diagnosed Pipeboard Meta Ads MCP as fully disconnected after a relink attempt (escalation from a mere weekly-cap error)

## Decisions
- None formally decided — diagnostic/drafting session, blocked before execution.

## Insights
- Ad disapprovals on this account should always be checked for "no credit check" / guaranteed-approval-style phrasing first — known Meta financial-services ad policy trigger. Also check `disable_all_enhancements` is set.
- Pipeboard free-plan weekly execution cap has now blocked mid-workflow twice (Jul 13, Jul 25). No fallback Meta connector exists — a Pro upgrade is the real fix if this keeps recurring.

## Open loops
- Push the drafted rewritten copy to ad `120251618482150248` once Meta connectivity is restored — copy is ready in the Jul 25 chat transcript, just needs `create_ad_creative` + `update_ad` run.
- Reconnect/fix the Pipeboard Meta Ads MCP connection — currently fully disconnected; may need a Pro upgrade to avoid the recurring weekly cap.
- RTG ad set (`120251560809090248`) still dark — carried forward, needs Ads Manager diagnostic.
- Instant Form (`2234033924078396`) still missing `privacy_policy_url` — carried forward.
- `special_ad_category` still mismatched on both live campaigns — carried forward.

## Artifacts
- None persisted — drafted ad copy exists only in this session's chat, not saved to an external file.

## Tools used
- Pipeboard Meta Ads MCP (failed/disconnected), ToolSearch, Supabase MCP, local memory files
