from typing import List
from bisect import bisect_left

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Step 1: Sort events by their start day
        events.sort()
        
        # Step 2: Extract only the start days for binary search purposes
        start_days = [event[0] for event in events]
        n = len(events)
        
        # Step 3: Memoization for DP
        dp = [[-1] * (k + 1) for _ in range(n)]
        
        # Define the recursive DP function
        def dfs(i, remaining):
            if i == n or remaining == 0:
                return 0
            if dp[i][remaining] != -1:
                return dp[i][remaining]
            
            # Option 1: Skip the current event
            max_val = dfs(i + 1, remaining)
            
            # Option 2: Take the current event
            next_event_idx = bisect_left(start_days, events[i][1] + 1)
            max_val = max(max_val, events[i][2] + dfs(next_event_idx, remaining - 1))
            
            # Memoize and return the result
            dp[i][remaining] = max_val
            return max_val
        
        # Start the recursion from the first event and maximum k events
        return dfs(0, k)
