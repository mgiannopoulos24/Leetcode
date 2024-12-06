class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        
        # Sort the nums array to use two-pointer technique
        nums.sort()
        
        # Precompute powers of 2 up to the length of nums
        n = len(nums)
        power_of_two = [1] * n
        for i in range(1, n):
            power_of_two[i] = (power_of_two[i - 1] * 2) % MOD
        
        left, right = 0, n - 1
        result = 0
        
        while left <= right:
            # Check if the current pair is valid
            if nums[left] + nums[right] <= target:
                # All subsequences between left and right are valid
                result += power_of_two[right - left]
                result %= MOD
                left += 1  # Expand the window by moving the left pointer
            else:
                right -= 1  # Shrink the window by moving the right pointer inward
                
        return result
