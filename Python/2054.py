from bisect import bisect_right

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by end time
        events.sort(key=lambda x: x[1])
        
        # Create a list of end times and a list of maximum values up to each event
        end_times = [event[1] for event in events]
        dp = [0] * len(events)
        dp[0] = events[0][2]
        
        # Fill dp array
        for i in range(1, len(events)):
            dp[i] = max(dp[i-1], events[i][2])
        
        max_sum = 0
        
        # Iterate through each event to find the maximum sum of two non-overlapping events
        for i in range(len(events)):
            current_start = events[i][0]
            current_value = events[i][2]
            
            # Find the latest event that ends before current_start
            j = bisect_right(end_times, current_start - 1)
            
            if j > 0:
                max_sum = max(max_sum, dp[j-1] + current_value)
            else:
                max_sum = max(max_sum, current_value)
        
        return max_sum