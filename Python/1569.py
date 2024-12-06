import math

MOD = 10**9 + 7

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        # Precompute factorials and inverse factorials up to the size of nums
        n = len(nums)
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        
        # Calculate all factorials % MOD
        for i in range(2, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        
        # Calculate inverse factorials using Fermat's little theorem
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD
        
        # Function to compute combination C(n, k) % MOD
        def comb(n, k):
            if k > n or k < 0:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD
        
        # Recursive function to compute the number of ways to reorder nums
        def count_ways(sub_nums):
            if len(sub_nums) <= 2:
                return 1  # Only one way to order a BST with 0, 1, or 2 nodes
            
            root = sub_nums[0]
            left = [x for x in sub_nums if x < root]
            right = [x for x in sub_nums if x > root]
            
            # Recursively compute the number of ways to order the left and right subtrees
            left_ways = count_ways(left)
            right_ways = count_ways(right)
            
            # Combine the results with the number of ways to interleave left and right subtrees
            return comb(len(left) + len(right), len(left)) * left_ways % MOD * right_ways % MOD
        
        # Subtract 1 because the original ordering is not counted as a reordering
        return (count_ways(nums) - 1) % MOD
