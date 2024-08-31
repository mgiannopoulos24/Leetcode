from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Append the current subset
            results.append(path[:])
            
            # Explore further subsets
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack to explore next subset
        
        results = []
        backtrack(0, [])
        return results