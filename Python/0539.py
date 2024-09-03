from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        # Convert all time points to minutes
        minutes_list = [time_to_minutes(tp) for tp in timePoints]
        
        # Sort the minutes
        minutes_list.sort()
        
        # Initialize minimum difference with a large value
        min_diff = float('inf')
        
        # Compare adjacent pairs
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
        
        # Compare last and first (circular difference)
        min_diff = min(min_diff, (1440 - minutes_list[-1] + minutes_list[0]))
        
        return min_diff
