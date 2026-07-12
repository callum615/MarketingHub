---
name: meta-ad-review
description: Review Meta (Facebook/Instagram) ad creatives for Galway Finance against AU credit compliance, creative quality, and Meta policy risk. Use when the user says "review my ad(s)," "check this ad," "ad review," "is this ad compliant," "audit my Meta ads," or shares an ad creative/design for feedback. Works on live ads pulled from the Meta account, Canva designs, or local image files.
---

# Meta Ad Review — Galway Finance

Review ad creatives through three lenses and produce a per-ad scorecard. This skill is **read-only against the ad account** — it never edits, pauses, or creates ads. Suggest fixes; the user applies them (or explicitly asks for changes afterwards).

## Required context (read first)

1. `.claude/AU-finance-compliance.md` — regulatory guardrails (non-negotiable)
2. `.agents/product-marketing.md` — positioning, brand voice, objections, disclosure rule

Key facts that recur in reviews:
- Corporate CRN **579221** (Galway Finance Pty Ltd) is used on business-published ads; individual CRN 579222 only for content in Callum's personal name.
- Standard disclosure line and comparison-rate rule are in the compliance file.
- All Galway campaigns touching housing/credit must use Meta's **HOUSING** special ad category (verify, don't assume).

## Step 1 — Get the creative(s)

Ask where the ad lives only if not obvious from the request:

**A. Live/paused ads in the Meta account** (default: `act_1928354054506891` "Galway Finance"):
1. `get_ads` (account, optionally filtered by campaign) → ad IDs + creative IDs
2. `get_ad_creatives(ad_id)` → headline, primary text, description, CTA, link
3. `get_ad_image` / `get_ad_previews` → visual; download or view the image for multimodal review
4. `get_campaign_details` / `get_adset_details` → objective, special ad category, targeting summary (needed for the policy lens)

**B. Canva designs**: `search-designs` → `get-design-thumbnail` or `export-design` → review the exported image. Ask for the intended copy (primary text/headline) since Canva only holds the visual.

**C. Local files**: Read the image path(s) directly. Ask for intended copy and placement if not supplied.

## Step 2 — Three-lens review

Review copy AND visual together (text inside the image counts as ad copy for compliance).

### Lens 1: AU credit compliance (hard gate — a fail here blocks publishing)
Work through the compliance file's pre-send checklist. Most common failures:
- Interest rate stated anywhere (including in the image) without comparison rate + representative example
- Missing/incorrect disclosure line or wrong CRN for the publisher
- "advice/advisor", "best loan", "guaranteed/instant approval", "lowest rate" framing
- Testimonial use without genuineness/incentive disclosure
- Outcome certainty implied ("you'll save $X") without "subject to lender approval" qualification

### Lens 2: Creative quality
Use the frameworks in the `ad-creative` skill (hook strength, one clear message, visual hierarchy, CTA clarity). Judge against the brand voice in `product-marketing.md`: straight-talking, plain English, no inflated claims. Check the ad answers a real objection or JTBD from the context doc rather than generic "great rates" filler.

### Lens 3: Meta policy risk
- **Special ad category**: campaign must be flagged HOUSING (housing-related) — credit-related lead ads also implicate the CREDIT category; flag if the campaign category looks wrong for the ad's content.
- **Personal attributes**: copy must not imply knowledge of the viewer's financial situation ("struggling with your mortgage?", "your debt", "you've been declined"). Rewrite to third-person or general framing.
- **Unrealistic outcomes**: savings claims, approval promises.
- **Image text**: heavy text overlays reduce delivery; flag walls of text in the visual.

## Step 3 — Output scorecard

One per ad:

```
## Ad: [name] (id)
Campaign: [name] · Objective · Special ad category: [X]

| Lens | Verdict | Notes |
|------|---------|-------|
| AU compliance | PASS / FLAG / FAIL | ... |
| Creative quality | score /10 | ... |
| Meta policy | LOW / MEDIUM / HIGH risk | ... |

**Must fix before running:** (compliance FAILs + HIGH policy risks)
**Should fix:** (FLAGs, quality issues)
**Suggested rewrite:** (only if must/should-fix items exist — provide compliant alternative copy)
```

End with a one-line overall verdict per ad: ship / fix then ship / pull.

## Rules

- Compliance verdicts cite the specific rule from the compliance file, not vibes.
- Never state that copy is "compliant" outright — say it "passes the working checklist; Purple Circle sign-off still applies."
- If performance data would change the recommendation (e.g. "pull this ad"), pull `get_insights` for the ad before recommending.
- Do not modify anything in the ad account. If the user asks to apply fixes, confirm the exact change first.
