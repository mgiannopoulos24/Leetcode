class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # Base case when n is 0
        if n == 0:
            return 0
        
        # Initialize the nums array of size n + 1
        nums = [0] * (n + 1)
        nums[1] = 1  # nums[1] is always 1
        
        # Generate the array according to the rules
        for i in range(1, (n // 2) + 1):
            if 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        
        # Return the maximum value in the array
        return max(nums)
