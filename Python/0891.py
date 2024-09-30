class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        
        # Precompute powers of 2 up to 2^n
        power_of_2 = [1] * n
        for i in range(1, n):
            power_of_2[i] = (power_of_2[i-1] * 2) % MOD
        
        total_width_sum = 0
        
        for i in range(n):
            max_contribution = nums[i] * power_of_2[i]
            min_contribution = nums[i] * power_of_2[n - i - 1]
            total_width_sum = (total_width_sum + max_contribution - min_contribution) % MOD
        
        return total_width_sum

