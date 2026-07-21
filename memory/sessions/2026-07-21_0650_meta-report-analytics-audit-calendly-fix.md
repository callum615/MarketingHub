# Session — 2026-07-21 — galway-finance

## Objective
Run the ad-hoc Meta Ads check-in, then investigate and fix the long-standing dead Lead/CompleteRegistration tracking gap via a full analytics audit.

## Summary
Pulled a 7-day Meta Ads report: zero real leads continue, and the retargeting Instant Form ad set showed genuinely zero impressions for 2+ full days (not just early ramp-up as previously assumed) despite everything reporting healthy via API. Callum spotted that the RTG ad set has Advantage+ audience disabled while the delivering cold ad set has it enabled — a plausible root cause given both custom_audience relaxation and advantage_audience are off, leaving almost no expansion room for two ~1000-person custom audiences. Ran a full GA4 + Meta Pixel tracking audit at Callum's request. Found GA4 mostly healthy but three phantom conversion events that never fire, and `generate_lead` firing but unmarked as a conversion. Chased the long-open dead Meta Lead/CompleteRegistration pixel: confirmed via Claude in Chrome that this account has no classic GTM container at all — the site uses Site Kit's native Google tag (gtag.js) plus a directly-embedded Meta Pixel. Root cause was a missing Calendly `event_scheduled` postMessage listener on the `/booking/` page. Implemented and verified a fix (added JS to the `page-booking` template's Custom HTML block), then marked `generate_lead` as a GA4 key event.

## Outcomes
- Meta Ads 7-day report delivered (Jul 13–20): zero real leads, spend $204.47
- Confirmed RTG ad set `120251560809090248` has had zero impressions for 2+ full days, not just early ramp-up
- Identified plausible root cause for RTG zero delivery: Advantage+ audience disabled + custom_audience relaxation disabled, unlike the delivering cold ad set
- Completed full GA4 + Meta Pixel tracking audit
- Root-caused the dead Meta Lead/CompleteRegistration event: missing Calendly `event_scheduled` listener on `/booking/`, not a GTM issue (confirmed no classic GTM container exists for this account)
- Implemented fix live: JS listener added to `page-booking` template's Custom HTML block (JavaScript tab), firing `fbq('track','Lead')` + `gtag('event','generate_lead')`
- Verified fix via live code inspection and a stubbed-function simulated Calendly event (no real event sent)
- Marked `generate_lead` as a GA4 key event (`conversionEvents/15296839842`, ONCE_PER_EVENT)
- Updated local `memory/open-loops.md` and `memory/projects/galway-finance.md`

## Decisions
- **No classic GTM for this account** — tracking is Site Kit's native Google tag (gtag.js, `GT-WV3W733W`) + a directly-embedded Meta Pixel. Future tracking edits go through the WordPress Site Editor's block templates, not tagmanager.google.com.
- **Fixed the dead Lead/CompleteRegistration pixel** via a Calendly postMessage listener added to the `page-booking` template's Custom HTML block.
- **`generate_lead` marked as GA4 key event** now that it has a real trigger behind it.

## Insights
- This account has no classic GTM container — don't check tagmanager.google.com for this site again.
- Custom HTML blocks in this site's block theme have separate HTML/CSS/JavaScript tabs via "Edit code" — use the JavaScript tab for page-scoped tracking code.
- Typing code directly into the live Site Editor via Claude in Chrome is blocked on the first attempt by an auto-mode safety classifier, even after in-chat authorization — needed an explicit re-confirmation from the user in exact terms before a retry succeeded.
- RTG ad set `120251560809090248` has `advantage_audience:0` and custom_audience relaxation `0` (no expansion allowed), while the delivering cold ad set has `advantage_audience:1` — plausible explanation for the zero-impression streak, flagged by Callum, not yet confirmed via Ads Manager diagnostics.

## Open loops
- Confirm a real Calendly booking produces the Lead event in Meta Events Manager and shows up in GA4 — code path proven, production not yet observed end-to-end
- Check RTG ad set `120251560809090248` delivery diagnostics in Ads Manager — test the Advantage+ audience hypothesis
- GA4 hygiene: remove 3 phantom conversion events (`purchase`, `close_convert_lead`, `qualify_lead`); consider marking `calculator_cta_click`/`contact_cta_click` as key events; add a custom dimension for loan-type/page-category
- Jul 24–26 Meta checkpoint (unchanged)
- Week-2 blog post overdue since Jul 20
- FB organic post ready, awaiting Callum to publish
- Special ad category still unset on both campaigns — Callum
- Instant Form question/notification review — Callum
- Define a target CPL or lead-volume goal — Callum

## Artifacts
- `page-booking` WordPress template — Custom HTML block JavaScript tab (Calendly tracking listener)
- GA4 conversion event `generate_lead` (`properties/541904526/conversionEvents/15296839842`)

## Tools used
Pipeboard Meta Ads MCP, Pipeboard GA4 MCP, Claude in Chrome browser automation, Supabase (local loader/saver), git
