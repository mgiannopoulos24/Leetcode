from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Compute F(0)
        F_0 = sum(i * num for i, num in enumerate(nums))
        
        # Compute sum of nums
        total_sum = sum(nums)
        
        # Initialize maximum with F(0)
        max_F = F_0
        
        # Compute F(k) from F(0) using the derived formula
        F_k = F_0
        for i in range(1, n):
            F_k += total_sum - n * nums[-i]
            max_F = max(max_F, F_k)
        
        return max_F
