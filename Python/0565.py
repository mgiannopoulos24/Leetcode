from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n  # To track visited indices
        max_length = 0
        
        for i in range(n):
            if not visited[i]:
                # Start a new cycle detection from index i
                current_length = 0
                x = i
                while not visited[x]:
                    visited[x] = True
                    x = nums[x]
                    current_length += 1
                max_length = max(max_length, current_length)
        
        return max_length
