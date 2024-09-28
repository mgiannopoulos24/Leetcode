from typing import List
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()  # Sort the array to process in increasing order
        dp = defaultdict(int)
        
        for x in arr:
            dp[x] = 1  # Each number can be a leaf node tree on its own
            for factor in arr:
                if factor * factor > x:
                    break
                if x % factor == 0:
                    quotient = x // factor
                    if quotient in dp:
                        if factor == quotient:
                            dp[x] += dp[factor] * dp[quotient]
                        else:
                            dp[x] += dp[factor] * dp[quotient] * 2
                        dp[x] %= MOD
        
        return sum(dp.values()) % MOD
