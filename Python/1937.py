from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev_row = points[0]  # Initial DP state (first row)
        
        for r in range(1, m):
            current_row = points[r]
            left = [0] * n
            right = [0] * n
            
            # Compute left-to-right maximum
            left[0] = prev_row[0]
            for c in range(1, n):
                left[c] = max(left[c - 1] - 1, prev_row[c])
            
            # Compute right-to-left maximum
            right[-1] = prev_row[-1]
            for c in range(n - 2, -1, -1):
                right[c] = max(right[c + 1] - 1, prev_row[c])
            
            # Update current row DP
            for c in range(n):
                current_row[c] += max(left[c], right[c])
            
            prev_row = current_row  # Move to the next row
        
        return max(prev_row)
