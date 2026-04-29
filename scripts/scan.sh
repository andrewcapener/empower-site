#!/bin/bash
# Security scan — checks live site for unauthorized external scripts

SITE_URL="https://empowereit.com"
APPROVED_DOMAINS=(
  "cdn.prod.website-files.com"
  "cdn.jsdelivr.net"
  "d3e54v103j8qbb.cloudfront.net"
  "fonts.googleapis.com"
  "fonts.gstatic.com"
  "www.googletagmanager.com"
  "www.google-analytics.com"
)

MALICIOUS_KNOWN=(
  "profitablecpmratenetwork"
  "highperformanceformat"
  "autoimageco"
)

echo "=== Empower EIT Security Scan — $(date) ==="
echo "Fetching: $SITE_URL"

PAGE=$(curl -sL "$SITE_URL")
if [ -z "$PAGE" ]; then
  echo "ERROR: Could not fetch $SITE_URL"
  exit 1
fi

FLAGGED=0

# Check for known malicious domains
echo ""
echo "--- Checking for known malicious domains ---"
for domain in "${MALICIOUS_KNOWN[@]}"; do
  if echo "$PAGE" | grep -qi "$domain"; then
    echo "ALERT: Malicious domain found — $domain"
    FLAGGED=1
  fi
done

# Extract all external script src domains
echo ""
echo "--- Checking all external script sources ---"
SCRIPTS=$(echo "$PAGE" | grep -oE 'src="https?://[^"]+' | sed 's/src="//')

while IFS= read -r script_url; do
  domain=$(echo "$script_url" | sed -E 's|https?://([^/]+).*|\1|')
  approved=false
  for approved_domain in "${APPROVED_DOMAINS[@]}"; do
    if [[ "$domain" == "$approved_domain" ]]; then
      approved=true
      break
    fi
  done
  if [ "$approved" = false ]; then
    echo "FLAGGED: Unapproved script domain — $domain ($script_url)"
    FLAGGED=1
  fi
done <<< "$SCRIPTS"

echo ""
if [ "$FLAGGED" -eq 0 ]; then
  echo "RESULT: CLEAN — No unauthorized scripts detected."
else
  echo "RESULT: ACTION REQUIRED — See flagged domains above."
fi

echo "=== Scan complete ==="
