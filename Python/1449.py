from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # Initialize DP array where dp[i] represents the maximum number of digits
        dp = [-1] * (target + 1)
        dp[0] = 0  # Base case: zero cost corresponds to zero digits

        # Iterate through each digit and update the DP array
        for i in range(1, 10):
            c = cost[i - 1]
            for j in range(c, target + 1):
                if dp[j - c] != -1:
                    dp[j] = max(dp[j], dp[j - c] + 1)

        # If it's impossible to form any number with the target cost
        if dp[target] == -1:
            return "0"

        # Construct the largest number by choosing the largest possible digit first
        result = []
        remaining = target
        for digit in range(9, 0, -1):
            c = cost[digit - 1]
            while remaining >= c and dp[remaining - c] == dp[remaining] - 1:
                result.append(str(digit))
                remaining -= c

        return ''.join(result)
