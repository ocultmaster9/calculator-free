// Canonical-host redirect for calculator-free.com
//
// Cloudflare Pages gives every project a free <project>.pages.dev address that
// cannot be switched off, and the custom domain is attached on top of the SAME
// deployment. That means the identical site answers on several hostnames
// (apex, www, and *.pages.dev). GA4 recorded real visitors arriving on the
// .pages.dev address in Aug 2026. A <link rel="canonical"> is a hint to search
// engines; this makes it a rule for browsers too.
//
// Canonical host for this site: calculator-free.com

const CANONICAL_HOST = 'calculator-free.com';

export async function onRequest(context) {
  const { request, next } = context;
  const url = new URL(request.url);

  if (url.hostname === CANONICAL_HOST) return next();
  if (url.hostname === 'localhost' || url.hostname === '127.0.0.1') return next();

  const target = new URL(url.pathname + url.search + url.hash, `https://${CANONICAL_HOST}`);
  return Response.redirect(target.toString(), 301);
}
