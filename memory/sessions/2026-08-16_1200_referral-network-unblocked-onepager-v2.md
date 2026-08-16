# Session — 2026-08-16 — galway-finance

## Objective
Decide the immediate marketing focus, then unblock and sharpen the referral-partner workstream.

## Summary
Callum asked what to focus on immediately. Recommended pivoting effort away from Meta ads and into the referral-partner network: Meta has spent ~$500+ since 2026-07-12 across 4+ account restructures and produced **zero leads ever**, CPC has gone $2.84 → $8.51, and at $15-20/day the account can't compete in the mortgage-broking auction. The campaigns are paused on funding anyway. Referral partners cost nothing and reach buyers at point of sale.

Pulling the actual Notion state revealed local memory was materially stale — `open-loops.md` listed the target prospect list and partner one-pager as untouched, but both had been drafted on 2026-07-26/27. The real bottleneck was a single Phase 0 task ("Confirm referral-relationship structure with Purple Circle") that had never been started and was 24 days overdue, gating every downstream outreach task. Callum confirmed the Purple Circle template is now sorted, clearing the gate.

Applied a Hormozi-style offer critique to the partner one-pager and rewrote it to v2. Also caught the compliance trigger phrase "no credit check from an initial enquiry" sitting in the draft — the same phrase that got Meta ad `120251618482150248` disapproved on 2026-07-22.

Callum then asked whether any of the top prospects had a broking business attached. Verification found two franchise-level finance arms the original research missed.

## Outcomes
- Agreed shift of immediate effort from Meta ads to referral partners
- Notion tracker: Phase 0 Purple Circle task → **Done**; title corrected from "reciprocal only, no fees" to commission-split
- Notion tracker: give-first referral task moved Phase 3 → **Phase 2, due 2026-08-19**, ahead of first outreach
- Partner one-pager rewritten to **v2** — reframed from company features to partner problem ("deals dying on the finance clause"), four checkable commitments, partner effort reduced to "send a name and a number", commission split moved down the page, per-partner-type value table added
- Compliance phrase "no credit check from an initial enquiry" stripped
- Phase 0 "what's in it for you" one-liner drafted: *"You send me a name and a number. I make sure the finance doesn't kill your deal, and you get paid when it settles."*
- Broking-conflict verification section added to the prospect list
- Outreach order revised

## Decisions
- **Immediate marketing focus = referral partners, not Meta ads.** Don't top up Meta budget until a target CPL exists.
- **Partner one-pager positions on deal-risk, not commission.** Every broker offers a split; competing there competes on the one axis where Galway Finance is identical to everyone else. A collapsed finance clause costs an agent a settlement worth many times any referral fee.
- **Give-first referral moves ahead of first outreach**, not after the relationship exists.
- **Purple Circle referral structure resolved** — commission-split template sorted, Phase 0 gate cleared.

## Insights
- For any franchised real estate or financial-services brand, check the **national group** for an in-house finance arm, not just the local office website. Century 21 Gold Key's own site never mentions CENTURY 21 Home Loans (ACL 388668); Professionals Northern Coast's never mentions Professionals Home Finance.
- Franchise finance arms aren't all equal. Ray White owns Loan Market outright with an exclusive day-one arrangement (hard exclusion). Century 21 and Professionals have group-level arms local offices may or may not use — ask, don't assume.
- An AFSL-only financial planner listing "mortgage planning" is a **stronger** prospect, not weaker — already having mortgage conversations, can't execute them.
- Local `memory/` drifted badly from Notion. When a workstream is tracked in a Notion database, read that database before trusting `open-loops.md`.
- A compliance phrase caught in one channel should be grepped across **all** drafted assets, not just fixed where it was found.
- Startup reported memory status as local-only, but Supabase (`vpmccpkhftzmmwhkensk`, ap-southeast-2) is ACTIVE_HEALTHY and queryable. The startup skill needs to actually attempt the query.

## Open loops
- Callum to read one-pager v2 and confirm the **same-business-day commitment is one he'll actually keep** — breaking it with a partner is worse than never making it
- Callum to sign off v2 copy; brand design pass still outstanding (content only)
- Ask Justin O'Connell (Century 21 Gold Key) and Professionals Northern Coast directly whether they already have a finance referral arrangement
- Confirm by phone that A&T Financial Advisers holds no credit licence (AFSL-only via Synchron Advice 243313)
- Draft outreach for the three cleared prospects
- Identify a current client to refer to Alkimos Tax or A&T, executing give-first before the ask
- Fix `/startup` so it queries Supabase as designed

## Artifacts
- [Referral Partner One-Pager (v2)](https://app.notion.com/p/3a9c844e9c4381119e22f7784ced6826)
- [Referral Network — Target Prospect List](https://app.notion.com/p/3aac844e9c438185b888c315a1afba8c)
- Referral Network Plan — Progress (`collection://27ab65ca-3564-46f4-8044-81cd1e1c2471`)
- Hormozi CMO persona memory: `~/.claude/projects/-Users-callumduffy-Documents-GitHub-MarketingHub/memory/reference_hormozi_cmo_project.md`

## Tools used
Notion MCP (search/fetch/query-data-sources/update-page) · WebSearch · WebFetch · Supabase MCP (list_projects/execute_sql)
