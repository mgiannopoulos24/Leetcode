class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # DP table to store the number of ways to arrange sticks
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Case 1: The tallest stick is visible
                dp[i][j] = dp[i - 1][j - 1]

                # Case 2: The tallest stick is not visible
                dp[i][j] += dp[i - 1][j] * (i - 1)

                dp[i][j] %= MOD

        return dp[n][k]
