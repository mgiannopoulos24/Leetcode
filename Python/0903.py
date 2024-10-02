class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        # dp[i][j] = number of ways to form valid permutations of length (i + 1) with last number j
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        dp[0][0] = 1  # There's exactly one way to form sequence of length 1 ending with 0

        for i in range(1, n + 1):
            if s[i - 1] == 'I':
                # Increasing, valid sequences of length i+1 that end in number j (0 <= j <= i)
                for j in range(1, i + 1):
                    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
            else:  # s[i - 1] == 'D'
                # Decreasing, valid sequences of length i+1 that end in number j (0 <= j <= i)
                for j in range(i - 1, -1, -1):
                    dp[i][j] = (dp[i][j + 1] + dp[i - 1][j]) % MOD

        # Sum all valid permutations of length n+1
        return sum(dp[n]) % MOD