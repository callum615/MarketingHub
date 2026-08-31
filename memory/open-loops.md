# Open loops — galway-finance

*Updated 2026-08-31 — connector strategy settled in principle; local memory had drifted 14 days behind Supabase again.*

> ⚠️ **Supabase is the source of truth, not this file.** On 2026-08-31 this worktree's local memory stopped at 2026-08-17 while Supabase was current to 2026-08-31, hiding two sessions including a 6-week reporting blackout. This is the third recorded drift instance. Always check Supabase `max(created_at)` at startup before trusting anything here.
> The referral workstream is tracked in the Notion DB "Referral Network Plan — Progress" (`collection://27ab65ca-3564-46f4-8044-81cd1e1c2471`) — read that before trusting the referral section below.

## ⚡ TOP PRIORITY (2026-08-31)
A. **Follow up the 3 referral outreach emails sent 2026-08-17** — Ben Carter (Alkimos Tax), Rachael (The Accounting Collective), Charné Humphreys (Shoebox Books). **14 days silent, no follow-up recorded.** This is the highest-leverage open item in the whole file: the channel is free, already in motion, and decaying. Owner: Callum/agent.
B. **Send or drop the A&T Financial Advisers (Tim Vander Kraats) Gmail draft** — still sitting unsent since 2026-08-17. Owner: Callum.

## Connectors & reporting — RESOLVED IN PRINCIPLE 2026-08-31
- ✅ **Do not pay for Pipeboard.** Verified live: the free native Meta connector reaches Galway Finance `1928354054506891` (ACTIVE, queryable). Pipedrive is a CRM, not a substitute for an ads connector.
- ✅ **Connector choice v2**: use Google's **official first-party read-only MCP servers** — `analytics-mcp` (GA4) and `google-ads-mcp` — **not AdvisorPPC** (community, write access, OAuth never worked). The AdvisorPPC decision is marked superseded in Supabase.
- 🔲 **Install GA4 server** — `claude mcp add analytics-mcp -- pipx run analytics-mcp`, then ADC with `analytics.readonly`. ~10 min, no approval gate. Awaiting Callum's go-ahead. Owner: agent.
- 🔲 **Confirm whether Google Ads spend actually exists** before pursuing a developer token (needs Explorer access via an MCC application). If there's no spend, skip it — GA4 alone closes the gap. Owner: Callum.
- ⚠️ **The scheduled-report blackout is NOT fixed by the above.** Both Google servers are **local stdio** — a cloud-scheduled run cannot reach a server on Callum's Mac. Must separately choose: (1) run the weekly report locally, (2) deploy to Cloud Run, or (3) hosted vendor. Owner: Callum decision, agent to execute.
- 🔲 **Personal Meta ad account `145431623` (USD) is DISABLED** — flagged for unusual activity, all ads paused. Business account unaffected. Contact Meta if the account is still wanted. Owner: Callum.
- 🔲 **Backfill local memory** with the 2026-08-24 and 2026-08-31 sessions, or formally accept Supabase as sole source of truth for this worktree. Owner: agent.

## STRATEGIC — self-employed repositioning (new 2026-08-16 evening)
Callum is repositioning Galway Finance around **self-employed clients**, as the natural path into asset and commercial finance. Sharpened to: tradies and small business owners in the northern growth corridor, on a home loan → asset finance → commercial ladder. `.agents/product-marketing.md` rewritten to V2; `.agents/content-strategy.md` pillar 5 promoted to anchor.

0a. **⛔ GATE — Purple Circle conversation. Blocks the whole expansion.** Confirm: (1) asset finance accreditation path, timeline, prerequisites; (2) commercial accreditation path + whether mentoring is mandatory; (3) **which alt-doc/self-employed lenders Callum is actually accredited with** — this is the product for this ICP and no honest capability claim can be made without it. Owner: Callum. Same shape as the referral-structure gate that silently blocked things for 24 days — do not let it sit.
0b. **Competitive check not done** — which Perth brokers already market to self-employed borrowers? That's the competitive set that matters now, and `product-marketing.md` has it flagged ⚠️. Owner: agent.
0d. **No self-employed service/landing page on the website** — the site still leads with first-home-buyer positioning. Gap. Owner: agent.
0e. **Add-backs comparison sheet** — how each of the top ~5 lenders treats depreciation, one-offs, additional super, non-recurring costs, interest on refinanced debt. Doubles as the single best leave-behind for an accountant. Gated on 0a(3). Owner: agent.

## URGENT — needs Callum confirmation
0c. ~~**Google Ads/GA4 connector (AdvisorPPC) setup parked**~~ — **SUPERSEDED 2026-08-31**, see Connectors section above; use the official Google servers instead. Original note: — Callum was connecting it himself via claude.ai Settings → Connectors, hit issues, parked 2026-08-09. Once connected it will also close the long-standing GA4 gap. Owner: Callum.
0f. **Scheduled weekly report returns Meta AND GA4 empty — now 6+ consecutive weeks (through 2026-08-31)**; root cause identified 2026-08-31 as scheduled sessions being unable to reach local/decommissioned servers, see Connectors section. Original note: — native Meta connector wasn't enabled for that scheduled-session context specifically (separate issue from the ad-hoc Pipeboard→native fix already shipped 2026-08-09). Needs fixing before next Monday's scheduled run. Owner: agent.

## Meta ads — in progress
1. **Push drafted compliant ad-copy rewrite to disapproved ad** `120251618482150248` (V1 Two Lenders hero, Test-Broad-Australia) via the native Meta connector (`ads_create_creative` + `ads_update_entity`). Copy is ready (removed the "no credit check" trigger phrase, fixed a hyper-local claim). Was blocked by Pipeboard's execution cap; native connector is now live and unblocked. Owner: agent.
2. **Instant Form UX audit** — nobody has reviewed the live form's (`2234033924078396`) actual question flow, friction, or completion message since the Jul19 Instant Form rebuild. Do this before concluding the zero-lead streak is a pure demand problem. Owner: agent.
3. **Instant Form missing `privacy_policy_url`** — confirmed empty via API. Compliance gap (not believed to block submissions technically, but still needs fixing). Owner: Callum/agent.
4. **special_ad_category mismatch** — both live campaigns still don't match the settled `FINANCIAL_PRODUCTS_SERVICES` (currently HOUSING / unset). API can't set post-creation — Ads Manager only. Owner: Callum.
5. **Define a target CPL or lead-volume goal** for the Meta campaigns — still no number in memory to judge go/no-go decisions against. Owner: Callum.
6. **Zero-lead streak** — now 10+ consecutive days across all campaigns despite Instant Form conversion (since the Jul19 rebuild). $170.28 spent this week (Jul19-25) alone. Treat as a stop-and-diagnose moment (form UX audit, not another wait cycle) before considering a full campaign pivot — account has been restructured 4+ times in 2 weeks, so "concept doesn't work" isn't a clean read yet. Owner: agent/Callum.
7. **ads_get_errors tool broken** in this environment — resolver error on every entity ID tried. Use `effective_status`/`delivery` substatus from `ads_get_ad_entities` instead until fixed. Owner: agent (workaround only, not a real fix).

## Ad creative refresh (Claude Design)
8. ~~Source real photography~~ — **done 2026-07-26**. No image-gen API available, but the `<image-slot>` component (drag-and-drop in the Claude Design canvas) solved it without one. V2 and V6 now have real Pexels stock photos (same photographer/shoot) set via `src`/`credit`.
9. **Manual Ads Manager creative swap needed to push new images live** — confirmed 2026-07-26 there is no safe API path (ad creatives immutable, no Instant Form param on `ads_create_creative`). Callum must duplicate each ad, replace the image, keep everything else identical, publish paused for review: V1 `120251560594890248`, V2 `120251560595390248`, V3 `120251560596170248`, V4 `120251560596630248`, V5 `120251560597530248`, RTG V6 `120251560810320248`, RTG V7 `120251560811000248`. Owner: Callum.
9b. **Get the 7 exported PNGs into Notion** — files ready at `/tmp/meta_ads_final/` (1080×1350, full-res). Notion page created: [Meta Ad Creative — Aligned Set (2026-07-26)](https://www.notion.so/Meta-Ad-Creative-Aligned-Set-2026-07-26-3a9c844e9c4381a5a20cfbf3f2871f4c). Callum to drag the 7 files into the "Images" section manually (automated upload proved impractical — see insight below). Owner: Callum. Note: files are in system temp, not durable — re-export from Claude Design if lost before this is done.
9c. **Build 1:1 square and 9:16 Stories/Reels versions** of all 7 ads — confirmed wanted, can proceed anytime now that the Meta push is manual (no longer blocking sequencing). Owner: agent.
10. **Cleanup — superseded ring-motif ad cards** — the first-pass redesign in the base Galway Finance Design System's `ads/` folder (meta-hero.card.html etc.) is now superseded by the aligned versions in "Galway Finance — Meta Ads". Low priority: remove or archive. Owner: agent, on explicit ask.
11. **Stock photo tone tradeoff** — V2/V6 house reads more upscale/architect-designed than a typical client's home; Callum accepted this consciously over geographically-mismatched modest alternatives. Revisit only if it becomes a real concern once ads are live.
12. **Optional cleanup** — 3 now-unused stock photos (`fhb-entrance.jpg`, `house-dusk.jpg`, `quote-pathway.jpg`) still in the design system, left in place for comparison. Low priority.

## Weekly report / reporting infrastructure
11. **Confirm the idempotency guard holds** — watch scheduled runs fire exactly once and behave correctly.
11a. **Meta pull bug fixed 2026-08-09** — `meta-report`/`weekly-marketing-report` had been silently failing to pull Meta data for 2 consecutive scheduled runs (stale Pipeboard `get_insights` tool reference). Fixed to use native `ads_get_ad_entities` with verified field names, tested live. Not yet run end-to-end as a full scheduled report — next Monday run is the real test. Owner: agent (monitor).
11b. **GA4 gap still open** *(fix path updated 2026-08-31: official `analytics-mcp`, not AdvisorPPC)* — no GA4 MCP tool connected in this environment; skill now documents this honestly instead of pointing at a phantom tool. Fix path: connect AdvisorPPC (see item 0c above), then wire GA4 fields into the skill.
11c. **Google Ads not yet in the weekly report at all** *(2026-08-31: first confirm any Google Ads spend exists before building this)* — once AdvisorPPC is connected, add a "Paid Search" section to `weekly-marketing-report` alongside Meta.

## Content
12. **Week-2 blog post** — "Construction Loans in WA: How Progress Payments Actually Work", due Jul20 — still overdue, still not started. Owner: agent. (V3 Construction is the ad-delivery workhorse — post + ad angle reinforce each other, though V3 is currently paused.)
13. **FB organic post** — "$100,000 apart" creative + caption ready; Callum to publish. Owner: Callum.
16. **Instagram square post for the FHB Grants & Schemes article** — 1080×1080 graphic built ([FB Post - FHB Grants and Schemes (1x1).dc.html](https://claude.ai/design/p/e5106aea-b312-446d-b2b9-49175d1de155?file=FB+Post+-+FHB+Grants+and+Schemes+%281x1%29.dc.html)), same caption/link as the FB post. Ready; Callum to post to Instagram. Owner: Callum.
17. **Other overdue posts**: "Is Refinancing Worth It" (~1.5wk overdue), "Self-Employed Home Loans" (~5 days overdue), "House-and-Land Packages in Perth's Northern Corridor" (due imminently) — all still at Idea stage. Owner: agent.

## Skills/docs hygiene
13a. **`/startup` skips Supabase** — the 2026-08-16 startup reported memory status as `local` only, but the Marketing Hub project (`vpmccpkhftzmmwhkensk`, ap-southeast-2) is ACTIVE_HEALTHY and queryable via the Supabase MCP the whole time. Startup must actually attempt the query instead of assuming no access — this is what let local memory drift 3 weeks without anyone noticing. Owner: agent.
14. **meta-ad-review SKILL.md stale** — still says HOUSING/CREDIT special ad category; settled decision is FINANCIAL_PRODUCTS_SERVICES. One-line fix. Owner: agent, on explicit ask.

## Referral network — NOW THE PRIMARY LEAD CHANNEL (unblocked 2026-08-16)
Settled 2026-08-16: this is where immediate marketing effort goes while Meta is paused. Meta has spent ~$500+ since Jul12 for zero leads ever; referral partners cost nothing and reach buyers at point of sale.

**Blocking Callum:**
15. **Read one-pager v2 and confirm the same-business-day commitment is one he'll actually keep** — it's the spine of the new positioning, and breaking it with a referral partner is worse than never promising it. Owner: Callum. ⬅ *do this before any outreach*
16. **Sign off one-pager v2 copy.** Content is final pending his read; brand design pass still outstanding. Owner: Callum.
17. **Identify a current client to refer to Alkimos Tax or A&T** — executes the give-first move (Notion task now Phase 2, due Aug19) before making any ask. Owner: Callum.

**Verification asks (do during first contact, not desk research):**
18. **Ask Justin O'Connell (Century 21 Gold Key) whether the office already has a finance referral arrangement** — Century 21 Australia runs CENTURY 21 Home Loans (Centurion Home Loans Services, ACL 388668), but the Clarkson office's own site never mentions it. Not an exclusion, an open question. Owner: Callum/agent.
19. **Same ask for Professionals Northern Coast** — Professionals Home Finance exists at group level. Owner: Callum/agent.
20. **Confirm A&T Financial Advisers holds no credit licence** — AFSL-only via Synchron Advice 243313, but they list "mortgage planning". If confirmed licence-free they're the strongest prospect on the list. Owner: agent (phone).

**Agent next:**
21. **Draft outreach messages** for cleared prospects. Owner: agent.
    - ~~Alkimos Tax Accounting (Ben Carter)~~ — drafted 2026-08-16, refined into Callum's own voice, **sent 2026-08-17** ("Coffee Catch Up"). First real outreach email of the referral workstream.
    - ~~The Accounting Collective Perth (Rachael)~~ — drafted and **sent 2026-08-17** ("Coffee Catch Up", same voice/template as Ben's).
    - **A&T Financial Advisers (Tim Vander Kraats)** — drafted 2026-08-17, sitting as a Gmail draft, **not yet sent**. Planner framing (lending sits alongside his strategy work), not the tax-tension wedge used for accountants.
    - **Enlighten Financial Services (Sarit Shah)** — drafted 2026-08-17, then **disregarded by Callum 2026-08-17** — do not send, do not follow up. Left as an orphaned Gmail draft (no delete-draft tool available in this environment). Reason flagged before disregarding: her LinkedIn lists "Senior Mortgage Broker" alongside planner, which would make her a direct competitor not a referral partner, though Enlighten's own site shows AFSL-only with no credit licence — never resolved either way.
    - ~~Shoebox Books and Tax (Charné Humphreys)~~ — new prospect, found 2026-08-17 (not on the original July list; corridor-wide coverage incl. Alkimos/Yanchep/Two Rocks/Butler/Eglinton/Jindalee, no finance/broking conflict). Personalized with a genuine parallel — Callum supplied Instagram/LinkedIn screenshots showing she launched Shoebox Books & Tax Joondalup in May 2026, same window as Galway Finance's own launch — and **sent 2026-08-17**.
    - **Success Tax Professionals Clarkson (Audrey de Beer)** — new prospect, found 2026-08-17, no finance conflict, 20+ years running Joondalup/Clarkson franchises. **Email not yet obtained** — WebFetch/WebSearch kept redacting the address; phone is (08) 9408 5908. Still needs either the real email from Callum or a phone-script approach.
    - Northern Beaches Realty, OmegaCA — still to draft.
    - **Add Shoebox Books and Tax + Success Tax Professionals Clarkson to the Notion Target Prospect List** — found this session, not yet logged there. Owner: agent, next touch.
21a. **Accountant-specific one-pager drafted** — [Referral Partner One-Pager — ACCOUNTANTS (v1)](https://app.notion.com/p/3bec844e9c4381ee8857cc9d78f1fbce). Leads with the tax-minimisation tension, adds a "when to send someone my way" trigger table, commits to never touching the tax position and never taking the client relationship. The general v2 one-pager is now effectively the **real-estate** variant. Awaiting Callum's sign-off + brand design pass. Note: its "referral never dead-ends" line depends on gate 0a.
21b. **Outreach voice correction, 2026-08-17:** Callum rewrote the Ben Carter draft substantially before sending — warmer, more personal ("I genuinely just love business," "untangling inter-entity loans"), subject line "Coffee Catch Up" not "Local broker, quick introduction." Subsequent A&T/Rachael/Sarit drafts were built to match this actual sent voice, not the original Notion outreach doc draft. **The Notion outreach doc (`Outreach — Alkimos Tax Accounting`) is now stale relative to what was actually sent — update it from the sent Gmail thread next time that page is touched.**
22. **Rank existing loose contacts by type/warmth** (was due Jul22, still not started). Owner: Callum.
23. **Scope a local networking group** (BNI/chamber) as a force-multiplier (was due Aug1). Owner: Callum.

Full 12-task plan lives in Notion "Referral Network Plan — Progress" — that DB is authoritative, not this list.

## Carried forward (unchanged)
21. **Purple Circle sign-off** on `.claude/AU-finance-compliance.md`. Owner: Callum.
22. **Privacy policy check** — Meta pixel remarketing coverage. Owner: Callum.
23. **product-marketing.md gaps** — metrics, verbatim customer language, named competitors.
24. **GA4 hygiene from 2026-07-21 audit**: three phantom conversion events (`purchase`, `close_convert_lead`, `qualify_lead`) marked as conversions but never fired — safe to unmark. Consider marking `calculator_cta_click`/`contact_cta_click` as key events, add a custom dimension for loan-type/page-category. Low priority.
25. **Confirm a real Calendly booking produces the Lead event end-to-end** in Meta Events Manager + GA4 — the Jul21 tracking fix's code path is proven but production has not been observed yet.

## Resolved this session (Aug16 afternoon)
- ~~Confirm referral-relationship structure with Purple Circle~~ — **Phase 0 gate CLEARED 2026-08-16**; commission-split template sorted. This single task had been blocking the entire referral workstream since Jul23.
- ~~Build target prospect list~~ — done 2026-07-27 (local memory had wrongly recorded this as untouched). 11 vetted prospects.
- ~~Create the partner one-pager~~ — drafted 2026-07-26, **rewritten to v2 2026-08-16** around partner deal-risk rather than company features.
- ~~Draft the "what's in it for you" one-liner~~ — *"You send me a name and a number. I make sure the finance doesn't kill your deal, and you get paid when it settles."*
- ~~Compliance phrase in partner one-pager~~ — "no credit check from an initial enquiry" stripped; same phrase that got Meta ad `120251618482150248` disapproved Jul22, propagated into the partner doc unnoticed.
- ~~Broking-conflict check on top prospects~~ — Century 21 + Professionals flagged (group-level finance arms); Alkimos Tax, A&T Financial, Northern Beaches Realty cleared.

## Resolved this session (Aug16)
- ~~Draft, fact-check + publish the "First Home Buyer Grants & Schemes in WA" hub post~~ — published at `/resources/first-home-buyer-grants-wa/` (WP post 73); fact-checked against primary sources, two errors caught and fixed.
- ~~Facebook post for the FHB Grants & Schemes article~~ — graphic + caption built, posted live by Callum.
- ~~Notion Content Library row stale (showed Editing despite... )~~ — n/a this row, but the row's Stage was corrected to Published after confirming live WP status.

## Resolved this session (Aug10)
- ~~Research + plan the 5% Deposit Scheme article~~ — standalone deep-dive scope confirmed (not the broader grants/schemes hub post).
- ~~Draft + stage the 5% Deposit Scheme article~~ — full copy, two Pexels images (no faces), staged as WP draft, compliance-checked.
- ~~Fix duplicate hero image, remove em-dashes, add "what happens if you move out" FAQ~~ — all applied per Callum's feedback.
- ~~Publish the 5% Deposit Scheme article~~ — live 2026-08-10 at `/resources/5-percent-deposit-scheme-wa/` (WP post 69), Notion row set to Published, per Callum's explicit confirmation.
- ~~Build a Facebook promotional graphic for the article~~ — built in Claude Design on the existing brand ad-template system, 1200×628, final headline "What is the 5% Deposit Scheme, and do you qualify?" after several rounds of options.

## Resolved this session (Aug9 afternoon)
- ~~Both Meta campaigns fully PAUSED account-wide~~ — confirmed intentional 2026-08-09: **ran out of budget/money**, not a technical or deliberate-strategy pause. Reactivation is a funding decision for Callum, not a diagnostic task — no further agent action until he tops up and reactivates.
- ~~Commit weekly-marketing-report Meta pull fix~~ — committed 2026-08-09 (`52fcfb3`), `meta-report/SKILL.md` + `weekly-marketing-report/SKILL.md`.

## Resolved this session (Jul25 afternoon)
- ~~Redesign ad creative visuals to remove photo dependency~~ — 5 of 7 Meta ad cards rewritten in Claude Design; graphic-only ring/typography treatment, copy preserved.
- ~~Diagnose whether a campaign pivot is warranted~~ — advised against it for now; recommended Instant Form UX audit + letting the account stabilize first.

## Resolved earlier (Jul23-25, reconstructed from Supabase)
- ~~Reconnect Meta Ads access after Pipeboard cap/disconnect~~ — Pipeboard fully decommissioned; native `mcp__claude_ai_Meta__*` connector confirmed live 2026-07-25.
- ~~Root-cause the disapproved ad~~ — "no credit check" trigger phrase + text_optimizations OPT_IN; compliant rewrite drafted 2026-07-25 (push still pending, see #1 above).
- ~~Confirm broader-Australia targeting + budget cut were intentional~~ — confirmed 2026-07-23, tied to Callum's possible relocation.
- ~~Execute Jul24-26 checkpoint ad-count cut~~ — done early, 2026-07-23 (V3/V5 paused, V1/V2/V4 kept active).
