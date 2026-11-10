Run started: 2026-11-10

Test results:
>> Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'SuperSecretAdminPassword123'
   Severity: Low   Confidence: Medium
   Location: insecure_app.py:5

>> Issue: [B602:subprocess_popen_with_shell_equals_true] subprocess call with shell=True identified, security issue.
   Severity: High   Confidence: High
   Location: insecure_app.py:14

>> Issue: [B311:blacklist] Standard pseudo-random generators are not suitable for security/cryptographic purposes.
   Severity: Low   Confidence: High
   Location: insecure_app.py:18

Code scanned: 23 lines. Total issues: 3 (High: 1, Low: 2)
