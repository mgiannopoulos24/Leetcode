class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by their left endpoint; if equal, by right endpoint in descending order
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Track the number of remaining intervals and the maximum right endpoint seen so far
        count = 0
        max_right = 0
        
        # Step 3: Iterate through the sorted intervals
        for left, right in intervals:
            # If this interval is not covered by the previous one (i.e., its right endpoint is larger)
            if right > max_right:
                count += 1  # This is a valid non-covered interval
                max_right = right  # Update the maximum right endpoint seen so far
        
        return count
