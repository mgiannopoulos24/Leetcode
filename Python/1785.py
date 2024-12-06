from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        # Step 1: Calculate the current sum of nums
        current_sum = sum(nums)
        
        # Step 2: Calculate the difference to reach the goal
        diff = abs(goal - current_sum)
        
        # Step 3: Calculate the minimum number of elements needed
        min_elements = (diff + limit - 1) // limit
        
        return min_elements
