from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Count the total number of 1's in the array
        k = sum(nums)
        
        # If there are no 1's, no swaps are needed
        if k == 0:
            return 0
        
        # Double the array to handle the circular condition
        nums = nums + nums
        
        # Initialize the count of 1's in the first window of size k
        ones_count = sum(nums[:k])
        
        # Initialize the minimum swaps as the number of 0's in the first window
        min_swaps = k - ones_count
        
        # Slide the window across the doubled array
        for i in range(len(nums) - k):
            # Update the count of 1's in the current window
            ones_count += nums[i + k] - nums[i]
            
            # Update the minimum number of swaps needed
            min_swaps = min(min_swaps, k - ones_count)
        
        return min_swaps
