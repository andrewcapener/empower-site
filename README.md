# Empower EIT — Website

Static site hosted on Cloudflare Pages. Migrated from Webflow April 2026.

**Live site:** https://empowereit.com  
**Cloudflare Pages URL:** https://empower-site.pages.dev  
**Contact:** Drew Capener — drewcapener.com

---

## Updating Content

1. Edit the relevant HTML file in `/public`
2. Commit the change:
   ```bash
   git add public/page-name.html
   git commit -m "Update: description of change"
   git push
   ```
3. Cloudflare Pages auto-deploys on every push to `main`. Live in ~30 seconds.

To roll back to any previous version:
```bash
git log                          # find the commit hash you want
git checkout <hash> -- public/   # restore that version of /public
git commit -m "Revert to <hash>"
git push
```

---

## Pages

| File | URL |
|------|-----|
| `index.html` | / |
| `about.html` | /about |
| `services.html` | /services |
| `projects.html` | /projects |
| `our-story.html` | /our-story |
| `sustainability.html` | /sustainability |
| `investment.html` | /investment |
| `leadership.html` | /leadership |
| `news.html` | /news |
| `faq.html` | /faq |
| `contact.html` | /contact |
| `legal.html` | /legal |

CMS pages (blog posts, team bios) are static HTML files — edit them directly in `/public`.

---

## Running the Security Scan

```bash
./scripts/scan.sh
```

Fetches the live site and checks all external scripts against the approved domain list. Outputs `CLEAN` or lists flagged domains. Run manually or add to a cron job:

```bash
# Run daily at 9am
0 9 * * * /path/to/empower-site/scripts/scan.sh >> /path/to/empower-site/backups/scan.log 2>&1
```

---

## Backups

```bash
./scripts/backup.sh
```

Mirrors the live site using `wget`, saves a timestamped snapshot to `/backups/YYYY-MM-DD/`, retains 30 days, and logs each run to `/backups/backup.log`.

**Restoring from backup:**
```bash
# Copy a backup snapshot back into /public
cp -r backups/2026-04-29/empowereit.com/* public/
git add public/
git commit -m "Restore from backup 2026-04-29"
git push
```

---

## Local Preview

```bash
npm run preview
```

Opens the site at http://localhost:3000.

---

## DNS Settings (Cloudflare Pages)

Point the domain's nameservers to Cloudflare:
```
ns1.cloudflare.com
ns2.cloudflare.com
```

Or add a CNAME record:
```
CNAME  @  empower-site.pages.dev
```

SSL is handled automatically by Cloudflare.

---

## Security

- Security headers applied to every page via `/public/_headers`
- All external scripts use `defer` for non-blocking load
- OG image self-hosted (no Webflow CDN dependency)
- Run `./scripts/scan.sh` any time to verify no unauthorized scripts
