# Security Review

## Name

security-review

## Description

Perform a security review of the codebase. Identify vulnerabilities, insecure patterns, and suggest fixes based on OWASP Top 10 and Python security best practices.

## Instructions

When performing a security review:

1. Check for **injection vulnerabilities** (SQL injection, command injection, path traversal)
2. Check for **insecure data handling** (hardcoded secrets, sensitive data in logs, missing input validation)
3. Check for **authentication/authorization issues** (missing auth, broken access control)
4. Check for **dependency vulnerabilities** (outdated packages, known CVEs)
5. Check for **misconfiguration** (debug mode in production, CORS too permissive, missing security headers)
6. Check for **insecure file operations** (unsafe path construction, unrestricted file uploads)

For each finding, provide:
- **Severity**: Critical / High / Medium / Low
- **Location**: File and line number
- **Issue**: What the problem is
- **Fix**: How to resolve it with a code example
