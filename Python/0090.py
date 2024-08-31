from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers to ensure duplicates are adjacent
        nums.sort()
        result = []
        subset = []
        
        def backtrack(start: int):
            # Add the current subset to the result
            result.append(subset[:])
            
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] in the current subset
                subset.append(nums[i])
                # Recurse with the next elements
                backtrack(i + 1)
                # Backtrack and remove nums[i] from the current subset
                subset.pop()
        
        # Start backtracking from the 0th index
        backtrack(0)
        return result