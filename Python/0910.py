class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        
        # Step 2: Initialize the result with the current max difference without any changes
        result = nums[-1] - nums[0]
        
        # Step 3: Try all possible splits
        for i in range(n - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i + 1] - k)
            result = min(result, high - low)
        
        return result
