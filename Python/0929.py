from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]  # take the part before the first '+'
            local = local.replace('.', '')  # remove all '.'
            canonical_email = f"{local}@{domain}"
            unique_emails.add(canonical_email)
        
        return len(unique_emails)
