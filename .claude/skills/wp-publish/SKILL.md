---
name: wp-publish
description: Stage a compliance-checked blog post or page as a DRAFT on galwayfinance.com.au via the WordPress.com MCP, with SEO title, meta description, and schema markup. Use when the user says "publish this post," "put this on the site," "stage this article," "push to WordPress," or a content pipeline reaches the publishing step. Never publishes live — always creates drafts for human review.
---

# WordPress Draft Publisher — Galway Finance

Take finished content and stage it on the site correctly: compliance-checked, SEO-complete, as a **draft**. The human publishes. No exceptions — this skill never sets `status: publish` and never updates a live page without explicit per-change confirmation.

Site: `galwayfinance.com.au` (WordPress.com Atomic, blog_id 254908544). A second free-plan site exists (`callume098cc9231-imynr.wordpress.com`) — never touch it; it's a leftover.

## Required context (read first)

1. `.claude/AU-finance-compliance.md` — pre-send checklist is mandatory
2. `.agents/product-marketing.md` — voice, terminology, disclosure rule (corporate CRN 579221 for site content)

## Step 1 — Compliance gate (before any MCP write)

Run the compliance file's pre-send checklist against the full draft. Hard blocks:
- Interest rate mentioned without comparison rate + representative example
- "advice/advisor" framing, "best loan/lowest rate" guarantees, approval certainty
- Missing general-information disclaimer for credit-related content
- Missing/incorrect disclosure line where the content promotes credit products

Append the standard footer to credit-related posts if absent:
> This information is general in nature and does not constitute financial, legal, tax or credit advice. Credit provided subject to lender approval and eligibility criteria. Galway Finance Pty Ltd ABN 34 697 469 551 (Credit Representative Number 579221) is a credit representative of Purple Circle Financial Services Pty Ltd ABN 21 611 305 170, Australian Credit Licence 486112.

If a hard block exists, stop and report it — do not stage a non-compliant draft "to fix later."

## Step 2 — SEO package

Prepare before creating:
- **Title** (≤60 chars, primary keyword near front) and **slug** (short, keyword, no stopwords)
- **Meta description** (140–155 chars, includes keyword + a reason to click)
- **Schema**: JSON-LD per the `schema` skill — `Article`/`BlogPosting` as baseline; `FAQPage` when the post has a genuine Q&A section; `LocalBusiness`/`FinancialService` only on relevant pages, not every post. Embed via a Custom HTML block at the end of the content.
- **Internal links**: at least one link to a relevant service page (e.g. /first-home-buyer-loans-perth/, /refinance-home-loan-perth/) and one to the booking page (/booking/) as the CTA.

## Step 3 — Stage the draft

Use `wpcom-mcp-content-authoring` on `galwayfinance.com.au`:
1. `posts.create` (or `pages.create` for evergreen pages) with `status: "draft"`, content as Gutenberg blocks (`describe` the operation first if unsure of the block format), categories/tags as appropriate.
2. The MCP requires `user_confirmed: true` for writes — describe exactly what will be created and get the user's yes first.
3. Return the **edit link and preview link** so Callum can review and hit publish himself.

For changes to an EXISTING page, use the block-level `page-sections.*` / `post-sections.*` operations to edit only the target section — never rewrite a whole live page for a small change, and always show the before/after of the section for confirmation first.

## Step 4 — Close the loop

- Report: title, slug, word count, compliance result ("passes working checklist; Purple Circle sign-off applies"), schema type used, preview link.
- Update the post's row in the Notion Content Library (data source `40dcbf2b-102f-4efc-837e-86f426e6fe03`): Stage → "Editing", set Live URL to the post's future permalink, and note the WP post ID in Notes. When Callum publishes, the row moves to "Published".

## Rules

- Drafts only. `status: "publish"` is forbidden even if asked casually — if Callum wants it live, he clicks publish, or explicitly confirms "publish it live now" in which case update the existing draft's status with a fresh confirmation.
- One post per confirmation — no bulk staging without listing every title first.
- GA4 note: property 541904526 currently has no booking/lead conversion event; don't promise measurement the setup can't deliver.
