class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        # Memoization dictionary to store the minimum number of operations
        memo = {}
        
        # Recursive function to compute the least number of operations
        def dp(target):
            if target == 0:
                return 0
            if target < x:
                # To express the number less than x, we either use:
                # 1. target * (1/x), which requires target addition operations
                # 2. (x - target) * (1/x), which requires (x - target) subtraction operations
                return min(2 * target - 1, 2 * (x - target))
            
            if target in memo:
                return memo[target]
            
            # Find the largest power of x that is <= target
            k = 0
            power = 1
            while power * x <= target:
                power *= x
                k += 1
            
            # Check if the target is exactly a power of x
            if power == target:
                # The number of operations is simply k - 1 for x^k
                memo[target] = k - 1
                return k - 1
            
            # Option 1: Try expressing target as x^k + remainder
            op1 = dp(target - power) + k
            
            # Option 2: Try expressing target as (x^(k+1) - target)
            # This works if we overshoot target and go up to x^(k+1)
            if power * x - target < target:
                op2 = dp(power * x - target) + k + 1
            else:
                op2 = float('inf')
            
            memo[target] = min(op1, op2)
            return memo[target]
        
        return dp(target)
