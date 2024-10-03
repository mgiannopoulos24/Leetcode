from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Create arrays to hold the maximum values up to each index and minimum values from each index
        max_left = [0] * n
        min_right = [0] * n
        
        # Fill max_left
        max_left[0] = nums[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], nums[i])
        
        # Fill min_right
        min_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        
        # Find the partition index
        for i in range(n - 1):
            if max_left[i] <= min_right[i + 1]:
                return i + 1