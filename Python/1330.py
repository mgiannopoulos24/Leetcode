class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Calculate the initial value of the array
        initial_value = 0
        for i in range(n - 1):
            initial_value += abs(nums[i] - nums[i + 1])
        
        # Step 2: Try reversing any subarray and calculate the potential improvement
        max_gain = 0
        
        # Special cases where the subarray starts at the beginning or ends at the last index
        for i in range(1, n - 1):
            max_gain = max(max_gain, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]))
            max_gain = max(max_gain, abs(nums[n - 1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))
        
        # General internal reversal optimization by tracking min and max for middle differences
        min_middle, max_middle = float('inf'), float('-inf')
        
        for i in range(1, n):
            min_middle = min(min_middle, max(nums[i - 1], nums[i]))
            max_middle = max(max_middle, min(nums[i - 1], nums[i]))
        
        max_gain = max(max_gain, 2 * (max_middle - min_middle))
        
        # Return the initial value plus the maximum possible gain
        return initial_value + max_gain
