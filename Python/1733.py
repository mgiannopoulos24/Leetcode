from typing import List
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Step 1: Convert languages list to a set-based structure for efficient lookups
        languages = [set(lang) for lang in languages]
        
        # Step 2: Identify uncommunicative friendships
        uncommunicative = set()
        for u, v in friendships:
            u -= 1
            v -= 1
            if not languages[u] & languages[v]:  # No common language
                uncommunicative.add(u)
                uncommunicative.add(v)
        
        # Step 3: Calculate teaching requirements
        min_teach = float('inf')
        for language in range(1, n + 1):
            # Count users who need to learn this language
            teach_count = sum(1 for user in uncommunicative if language not in languages[user])
            min_teach = min(min_teach, teach_count)
        
        return min_teach
