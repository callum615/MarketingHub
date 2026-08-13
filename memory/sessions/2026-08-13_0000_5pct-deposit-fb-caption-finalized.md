# Session — 2026-08-13 — galway-finance

## Objective
Produce a Facebook caption to accompany the already-built 5% Deposit Scheme article graphic.

## Summary
Verified the "FB Post - 5pct Deposit Scheme.dc.html" graphic (built 2026-08-10 in the Social media ad templates Claude Design project) was still intact and unchanged. Drafted three caption options compliant with AU finance guardrails (no rate quoted, so no comparison-rate/disclosure line needed; no advice-framing; no guaranteed-outcome claims). Callum selected Option B (question-led, matches the graphic's headline). Startup also surfaced a local-memory gap: the 2026-08-10 00:24 scheduled weekly-marketing-report run (found in Supabase, not previously logged locally) came back with both Meta and GA4 empty — the native Meta connector wasn't enabled for that scheduled-session context specifically, separate from the ad-hoc meta-report fix already shipped 2026-08-09.

## Outcomes
- Facebook caption finalized: Option B (question-led)
- FB post now fully ready to publish (graphic + caption) — only Callum's manual post action remains

## Decisions
- **5% Deposit Scheme FB caption**: "Thinking a 5% deposit sounds too good to be true? Here's exactly how the government's Home Guarantee Scheme works in WA — who qualifies, the price caps in Perth and regional areas, and the honest trade-offs most guides skip." — chosen over a direct-informational and a short/scroll-stopping alternative.

## Insights
- No new lessons this session; confirmed prior finding that a link-post caption with no rate quoted doesn't need the standard credit disclosure line (that's tied to ads/pages quoting rates or credit products specifically).

## Open loops
- Callum to post the finalized FB post (graphic + Option B caption) to Facebook — no posting capability in this environment.
- Scheduled-session Meta connector gap (2026-08-10 00:24 run: GA4/Meta both empty) still needs fixing — separate from the ad-hoc meta-report fix already shipped. Not touched this session.
- Carried forward unchanged: Meta campaigns paused pending Callum's budget top-up; AdvisorPPC OAuth parked on Callum's end; 3 overdue blog posts (Construction Loans ~1 month, FHB Grants/Schemes hub ~3 weeks, Is Refinancing Worth It); FB "$100,000 apart" organic post still awaiting Callum; referral network paperwork/contact ranking; Notion hygiene fix for "How Much Can I Borrow?" Stage.

## Artifacts
- FB Post - 5pct Deposit Scheme.dc.html (Claude Design, project `e5106aea-b312-446d-b2b9-49175d1de155`) — caption now attached in Supabase artifact record, no file changes needed.

## Tools used
- Claude Design MCP, Supabase MCP
