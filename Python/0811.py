from typing import List
from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_count = defaultdict(int)
        
        for entry in cpdomains:
            count, domain = entry.split(' ')
            count = int(count)
            parts = domain.split('.')
            
            # Generate all subdomains
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                domain_count[subdomain] += count
        
        # Format the result
        result = [f"{count} {domain}" for domain, count in domain_count.items()]
        return result
