class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Create a sorted list of indices based on the values of nums
        sorted_indices = sorted(range(n), key=lambda i: nums[i])
        
        # Step 2: Initialize variables to track the maximum width of a ramp
        max_width = 0
        min_index = float('inf')
        
        # Step 3: Iterate over the sorted indices
        for i in sorted_indices:
            # Calculate the ramp width as current index `i` - the smallest index seen so far
            max_width = max(max_width, i - min_index)
            
            # Update the minimum index encountered so far
            min_index = min(min_index, i)
        
        return max_width
