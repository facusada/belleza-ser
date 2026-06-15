export default defineEventHandler((event) => {
  const siteUrl = useRuntimeConfig().public.siteUrl
  setHeader(event, 'Content-Type', 'text/plain')
  return `User-agent: *\nAllow: /\n\nSitemap: ${siteUrl}/sitemap.xml\n`
})
