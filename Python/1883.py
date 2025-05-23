from typing import List
from decimal import Decimal, getcontext, ROUND_CEILING
import math

# Set high precision to prevent rounding errors
getcontext().prec = 50

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = Decimal('Infinity')
        
        # dp[k] = minimum time to reach current road using k skips
        dp = [INF] * (n + 1)
        dp[0] = Decimal(0)  # Start at time 0 with 0 skips
        
        # Precompute travel times for each road
        travel_times = [Decimal(d) / Decimal(speed) for d in dist]
        
        for i in range(n):
            ndp = [INF] * (n + 1)
            
            for skips in range(n + 1):
                if dp[skips] == INF:
                    continue
                
                current_time = dp[skips]
                travel_time = travel_times[i]
                
                # Option 1: Do not skip rest (round up unless it's the last road)
                new_time = current_time + travel_time
                if i != n - 1:
                    # Must wait until next integer hour => ceil
                    new_time_ceil = new_time.to_integral(rounding=ROUND_CEILING)
                    ndp[skips] = min(ndp[skips], new_time_ceil)
                else:
                    # Last road, no need to wait
                    ndp[skips] = min(ndp[skips], new_time)
                
                # Option 2: Skip rest (only possible if not last road)
                if i != n - 1 and skips < n:
                    new_time_skipped = current_time + travel_time
                    ndp[skips + 1] = min(ndp[skips + 1], new_time_skipped)
            
            dp = ndp
        
        # Find the minimum number of skips required
        for skips in range(n + 1):
            if dp[skips] <= Decimal(hoursBefore):
                return skips
        return -1