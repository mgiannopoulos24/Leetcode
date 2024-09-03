from bisect import bisect_left
from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Create a sorted list of (start_time, index)
        starts = sorted((start, i) for i, (start, end) in enumerate(intervals))
        
        result = []
        
        # For each interval, find the right interval using binary search
        for start, end in intervals:
            # Find the smallest start time >= end time
            index = bisect_left(starts, (end, -1))
            
            if index < len(starts):
                result.append(starts[index][1])
            else:
                result.append(-1)
        
        return result
