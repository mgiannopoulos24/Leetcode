from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Combine the jobs into a list of tuples and sort them by end time
        jobs = sorted(zip(endTime, startTime, profit), key=lambda x: x[0])
        n = len(jobs)
        
        # Extract the sorted end times for binary search
        sorted_end_times = [job[0] for job in jobs]
        
        # Initialize DP array where dp[i] represents the max profit up to job i
        dp = [0] * (n + 1)  # dp[0] = 0 as base case
        
        for i in range(1, n + 1):
            current_end, current_start, current_profit = jobs[i - 1]
            # Find the last job that doesn't conflict with the current job
            j = bisect.bisect_right(sorted_end_times, current_start) - 1
            if j >= 0:
                dp[i] = max(dp[i - 1], current_profit + dp[j + 1])
            else:
                dp[i] = max(dp[i - 1], current_profit)
        
        return dp[n]
