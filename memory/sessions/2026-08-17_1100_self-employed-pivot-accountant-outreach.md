# Session — 2026-08-17 — galway-finance

## Objective
Reposition Galway Finance's marketing around self-employed borrowers (Callum's stated new focus), rebuild the foundational context docs around it, and execute the first round of real accountant/planner referral outreach.

## Summary
Callum said he wants to build the business around self-employed clients, as a natural path into asset and commercial finance (home loan → asset finance → commercial, one client acquisition amortised across a decade). Rewrote `.agents/product-marketing.md` to V2 around this ICP (self-employed retained FHB as a real secondary segment, not deleted), added a hard compliance boundary — never advise on tax positions, only their lending consequence — and promoted Pillar 5 in `.agents/content-strategy.md` to the anchor content pillar. Built an accountant-specific referral one-pager (leads with the tax-minimisation-vs-borrowing-capacity tension, not the real-estate "finance clause" framing used in the existing v2) and a first outreach draft for Alkimos Tax Accounting.

Session then moved into live execution via the Gmail connector: drafted, Callum personally rewrote (warmer, more specific — "I genuinely just love business," "untangling inter-entity loans"), and sent the first real outreach email to Ben Carter (Alkimos Tax). Matched that actual sent voice for all subsequent drafts rather than the original Notion doc's more formal draft. Drafted and sent to Rachael (The Accounting Collective Perth). Drafted for Sarit Shah (Enlighten Financial Services) but flagged a conflict signal — her LinkedIn lists "Senior Mortgage Broker" alongside planner, which would make her a competitor not a partner, though the firm's own site shows AFSL-only — Callum disregarded her without resolving the discrepancy either way. Drafted for Tim Vander Kraats (A&T Financial Advisers, planner framing) — not yet sent. Searched for additional local accountants beyond the original July list; found Shoebox Books and Tax (Charné Humphreys, corridor-wide coverage) and Success Tax Professionals Clarkson (Audrey de Beer), both clear of finance conflicts. Callum supplied Charné's email plus Instagram/LinkedIn screenshots showing she launched Shoebox Books & Tax Joondalup in May 2026 — same window as Galway Finance's own launch — personalized the email around that genuine parallel, and it was sent.

## Outcomes
- `.agents/product-marketing.md` rewritten to V2 — self-employed primary ICP, FHB retained as secondary, tax-advice compliance boundary added, accountant partner persona added
- `.agents/content-strategy.md` — Pillar 5 (self-employed) promoted to anchor, full content cluster mapped
- [Referral Partner One-Pager — ACCOUNTANTS (v1)](https://app.notion.com/p/3bec844e9c4381ee8857cc9d78f1fbce) created — accountant-specific variant, leads with tax-minimisation tension, trigger table for when to refer
- [Outreach — Alkimos Tax Accounting (DRAFT v1)](https://app.notion.com/p/3bec844e9c438199aa1dd2381d24d0d2) created — now stale relative to what was actually sent (see insights)
- 3 real outreach emails sent via Gmail: Ben Carter (Alkimos Tax), Rachael (The Accounting Collective Perth), Charné Humphreys (Shoebox Books and Tax)
- 1 email drafted, awaiting Callum's send: Tim Vander Kraats (A&T Financial Advisers)
- 1 email drafted then disregarded: Sarit Shah (Enlighten Financial Services) — orphaned Gmail draft, no delete-draft tool available
- 2 new prospects sourced and vetted (not on the original July list): Shoebox Books and Tax, Success Tax Professionals Clarkson — not yet added to the Notion Target Prospect List

## Decisions
- **Primary ICP shift: self-employed borrowers**, sharpened to tradies/small business owners in the northern growth corridor, on a home→asset→commercial ladder. FHB stays served but de-prioritised for new marketing investment.
- **Tax boundary is absolute**: content and partner material give lending consequences only, never tax-position advice — protects both the compliance line and the accountant-referral relationship.
- **Outreach voice = Callum's own edited version**, not the original Notion draft — warmer, more personal, subject line "Coffee Catch Up." All subsequent drafts matched this.
- **No commission split or one-pager attachment in first-contact outreach** — carried over from the original outreach doc's reasoning, still applied in every sent email.
- **Sarit Shah disregarded** without resolving the mortgage-broker conflict signal — treated as closed, not paused.

## Insights
- WebFetch/WebSearch reliably redact scraped email addresses in their summarized output even when the source page shows them in full — got a usable address for Success Tax Professionals Clarkson from search snippets but couldn't extract a clean, confident copy; ended up blocked on Callum supplying it directly. Consider trying a more targeted fetch prompt or a second source next time this happens rather than treating one masked result as final.
- Franchise/group finance-arm conflict checking (established 2026-08-16) needs to extend to **individual professional titles on LinkedIn**, not just company names — Sarit Shah's personal "Senior Mortgage Broker" title wasn't visible from the business's own website at all.
- The Notion outreach doc (`Outreach — Alkimos Tax Accounting`) documents a draft that was substantially rewritten by Callum before sending — it's now a stale record of the *intended* approach, not what actually went out. Worth updating from the sent Gmail thread next time that page is touched, or treating Notion drafts as a starting point rather than a source of truth once real sends diverge from them.
- Personal/social context (Instagram bio posts, LinkedIn job history) that Callum supplies directly can produce sharper personalization than public business-site research alone — the "launched around the same time" parallel with Charné came entirely from screenshots he provided, not from anything discoverable via web search.

## Open loops
- **Purple Circle gate (0a)** — asset/commercial accreditation path and the alt-doc lender panel, still unconfirmed. Blocks the "never dead-ends" claim in both one-pagers and the ladder-expansion strategy generally.
- **Competitive check (0b)** — which Perth brokers already market to self-employed borrowers, still not done.
- Send or drop the A&T Financial Advisers (Tim Vander Kraats) draft.
- Get Success Tax Professionals Clarkson's real email (or switch to a phone script) and draft outreach.
- Draft outreach for Northern Beaches Realty and OmegaCA (both cleared, not yet drafted).
- Add Shoebox Books and Tax and Success Tax Professionals Clarkson to the Notion Target Prospect List.
- Update the Notion outreach doc to reflect the actual sent voice, or note it's now a stale first draft.
- Identify a current client to refer to Alkimos Tax or A&T — give-first move, was due 2026-08-19 (may now be moot for Alkimos Tax since outreach already went out ahead of it).

## Artifacts
- `.agents/product-marketing.md` (V2, rewritten)
- `.agents/content-strategy.md` (Pillar 5 promoted)
- [Referral Partner One-Pager — ACCOUNTANTS (v1)](https://app.notion.com/p/3bec844e9c4381ee8857cc9d78f1fbce)
- [Outreach — Alkimos Tax Accounting (DRAFT v1)](https://app.notion.com/p/3bec844e9c438199aa1dd2381d24d0d2) — stale, see insights
- 3 sent Gmail threads (Ben Carter, Rachael, Charné Humphreys), 2 drafts (A&T, Sarit — Sarit disregarded)

## Tools used
Supabase MCP (execute_sql) · Notion MCP (fetch/create-pages) · Gmail MCP (create_draft/update_draft/search_threads/get_thread) · WebFetch · WebSearch
