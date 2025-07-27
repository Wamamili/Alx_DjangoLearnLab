# Security Measures

- XSS, Clickjacking, and MIME-sniffing protections are enabled.
- CSRF and session cookies are secure (HTTPS-only).
- All forms use CSRF tokens.
- ORM is used exclusively for database interactions.
- Content Security Policy (CSP) is enforced via django-csp.
