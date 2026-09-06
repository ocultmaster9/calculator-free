# calculator-free.com

Static site on Cloudflare Pages. **Push to `main` = deploy to production.**

## Rules (learned the hard way)
- This site has its OWN repo, OWN pipeline, OWN GA4 tag (G-Q7VYR4L8Z7) and OWN
  scoped Cloudflare token. Never shared with another site — one site must never
  be able to break another.
- Canonical host is **calculator-free.com**. `functions/_middleware.js` 301s every other
  hostname (apex/www/*.pages.dev) to it. CI asserts that redirect on every deploy.
- A static check cannot prove a page works. Anything JS-rendered must be opened
  in a real browser before it counts as done.

## Deploy
Run `PUSH-calculator-free.cmd` on the Desktop. All output goes to a log file —
a bare terminal window is invisible and failures went unseen that way before.

## Required repo secrets
- `CLOUDFLARE_API_TOKEN` — scoped token that covers calculator-free.com
- `CLOUDFLARE_ACCOUNT_ID` — ec88bed5c04209eb4da62f848e803d31
