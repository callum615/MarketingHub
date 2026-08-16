# Session — 2026-08-16 — galway-finance

## Objective
Draft, fact-check, and publish the queued "First Home Buyer Grants & Schemes in WA" hub post, plus build matching Facebook/Instagram social assets.

## Summary
Drafted and staged the overdue "First Home Buyer Grants & Schemes in WA (2026)" hub post (WP post 73) covering FHOG, stamp duty concessions, the 5% Deposit Scheme (linked to the existing deep-dive), and Keystart. Fact-checked every claim against primary sources (wa.gov.au, firsthomebuyers.gov.au, keystart.com.au), catching and fixing two real errors from the first draft: a wrong historical stamp duty threshold and an invented Keystart shared-equity product name ("Urban Connect", corrected to the real "SharedStart"). Sourced and vetted two Pexels images (rejected North-American-style and inappropriately upscale candidates), uploaded via browser to avoid base64 cost, and inserted them via the WordPress MCP's section-level API after browser scroll automation broke mid-session (a literal "Page_Down" key name got typed into the post body as text — caught and undone before saving, no data loss). Callum published the article live himself. Built matching Facebook (1200×628) and Instagram (1080×1080) graphics in Claude Design on the existing brand template system, fixed an unbalanced empty-space layout issue in the square version, and finalized a compliance-checked caption (question-led, em-dash removed per Callum's ask). Callum has posted the Facebook version live; the Instagram square graphic is ready but not yet posted. Notion Content Library row corrected to Published after confirming live status via the WordPress API — Callum had published without looping the agent in, so the row was stale until checked.

## Outcomes
- Published: https://galwayfinance.com.au/resources/first-home-buyer-grants-wa/ (WP post 73)
- Notion Content Library row corrected to Published
- Facebook post graphic (1200×628) and Instagram square graphic (1080×1080) built in Claude Design
- Facebook post live (per Callum); Instagram square ready to post

## Decisions
- **FHB Grants & Schemes hub post prioritized this week** over the more-overdue Construction Loans article — compounds with the freshly-published 5% Deposit Scheme article via internal linking; Construction Loans ties to a currently paused ad set, so less immediate payoff.
- **Cut the unverifiable historical stamp duty comparison line** rather than publish a number that couldn't be cleanly verified — third-party blogs said $500k, wa.gov.au's own change-history page showed $450k for the immediately-prior period.
- **Keystart shared-equity product corrected to "SharedStart"** (with GoodStart and Sole Parent variants), replacing an invented "Urban Connect" name from the first draft.

## Insights
- Third-party finance/broker blogs are unreliable for exact historical or current WA stamp duty and Keystart figures — some directly contradict primary sources. Always verify numeric claims for regulated content against primary source pages (wa.gov.au announcement pages, firsthomebuyers.gov.au, keystart.com.au), not aggregator blogs.
- `claude-in-chrome`'s `computer` tool `key` action does not interpret multi-word key names like "Page_Down" as navigation keys inside the WordPress Gutenberg editor — it gets typed as literal text into the focused block. Use mouse `scroll` instead, or better: avoid browser scroll+click for content edits entirely and use the WordPress MCP's `post-sections.list/insert/replace` tools (block-level edits with optimistic locking via etag/content_hash) — far more reliable for inserting images or sections into an existing post.
- Notion Content Library Stage can drift from actual WordPress status when Callum publishes directly via wp-admin without looping the agent in. Worth a quick `posts.get` status check before wrap-up whenever a "Callum will publish" open loop was left from earlier in the session.

## Open loops
- **Instagram square post** — Callum to post the ready 1080×1080 graphic (same caption/link as the Facebook post). Owner: Callum.
- Construction Loans in WA article — still overdue (~4 weeks), not started. Owner: agent.
- Is Refinancing Worth It — overdue (~1.5 weeks). Owner: agent.
- Self-Employed Home Loans — overdue (~5 days). Owner: agent.
- House-and-Land Packages — due imminently. Owner: agent.
- FB organic "$100,000 apart" post — still awaiting Callum to publish (carried from earlier).

## Artifacts
- WP post 73 — First Home Buyer Grants & Schemes in WA (2026), published, https://galwayfinance.com.au/resources/first-home-buyer-grants-wa/
- Claude Design: [FB Post - FHB Grants and Schemes.dc.html](https://claude.ai/design/p/e5106aea-b312-446d-b2b9-49175d1de155?file=FB+Post+-+FHB+Grants+and+Schemes.dc.html) (1200×628, posted live)
- Claude Design: [FB Post - FHB Grants and Schemes (1x1).dc.html](https://claude.ai/design/p/e5106aea-b312-446d-b2b9-49175d1de155?file=FB+Post+-+FHB+Grants+and+Schemes+%281x1%29.dc.html) (1080×1080, ready)
- Media 74 (featured image, aerial Australian suburb rooftops) and Media 77 (in-post image, single-storey tile-roof home) on galwayfinance.com.au

## Tools used
- wpcom-mcp-content-authoring (WordPress), Claude Design MCP, claude-in-chrome browser automation, WebFetch/WebSearch, Notion MCP, Supabase MCP
