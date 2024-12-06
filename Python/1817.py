from typing import List
from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # Step 1: Calculate unique active minutes (UAM) for each user
        user_minutes = defaultdict(set)
        for user_id, time in logs:
            user_minutes[user_id].add(time)
        
        # Step 2: Count the frequency of each UAM
        uam_counts = [0] * k
        for minutes in user_minutes.values():
            uam = len(minutes)
            if 1 <= uam <= k:
                uam_counts[uam - 1] += 1

        return uam_counts
