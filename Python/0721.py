from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Helper functions for Union-Find (Disjoint Set Union)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # Initialize the Union-Find structure
        parent = {}
        email_to_name = {}
        
        # Process each account
        for account in accounts:
            name = account[0]
            first_email = account[1]
            
            if first_email not in parent:
                parent[first_email] = first_email
            
            email_to_name[first_email] = name
            
            for email in account[2:]:
                if email not in parent:
                    parent[email] = email
                
                # Union the current email with the first email of the account
                union(first_email, email)
                
                # Map email to the name
                email_to_name[email] = name
        
        # Collect emails by their root representative
        root_to_emails = defaultdict(list)
        for email in parent:
            root = find(email)
            root_to_emails[root].append(email)
        
        # Format the result
        result = []
        for root, emails in root_to_emails.items():
            result.append([email_to_name[root]] + sorted(emails))
        
        return result