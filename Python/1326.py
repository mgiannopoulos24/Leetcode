class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Step 1: Convert ranges into intervals [left, right]
        intervals = []
        for i in range(n + 1):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            intervals.append((left, right))
        
        # Step 2: Sort intervals by the starting point (left)
        intervals.sort()
        
        # Step 3: Use a greedy approach to cover the garden
        taps_opened = 0
        current_end = 0
        next_end = 0
        i = 0
        
        while current_end < n:
            # Try to extend the range [0, current_end] as far as possible
            while i <= n and intervals[i][0] <= current_end:
                next_end = max(next_end, intervals[i][1])
                i += 1
            
            # If we cannot extend the current range, return -1
            if next_end == current_end:
                return -1
            
            # Open the tap that extends the furthest
            taps_opened += 1
            current_end = next_end
        
        return taps_opened
