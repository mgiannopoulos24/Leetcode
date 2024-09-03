from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        # Initialize variables
        count_removed = 0
        last_end = intervals[0][1]
        
        # Iterate through sorted intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < last_end:
                # If there is an overlap, increment the count of removed intervals
                count_removed += 1
            else:
                # Update the end time of the last interval added to the non-overlapping set
                last_end = end
        
        return count_removed
