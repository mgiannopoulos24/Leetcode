from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        dq = deque()
        max_value = float('-inf')
        
        for x, y in points:
            # Remove points from the deque if their x difference is greater than k
            while dq and x - dq[0][1] > k:
                dq.popleft()
            
            # If there's a valid point in the deque, calculate the potential maximum value
            if dq:
                max_value = max(max_value, dq[0][0] + y + x)
            
            # Add the current point to the deque, maintaining decreasing order of (y - x)
            while dq and dq[-1][0] <= y - x:
                dq.pop()
            dq.append((y - x, x))
        
        return max_value
