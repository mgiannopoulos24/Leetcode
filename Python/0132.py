class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Step 1: Precompute palindrome substrings
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for length in range(2, n + 1):  # length of the substring
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    is_palindrome[start][end] = (s[start] == s[end])
                else:
                    is_palindrome[start][end] = (s[start] == s[end]) and is_palindrome[start + 1][end - 1]
        
        # Step 2: Compute minimum cuts
        dp = [float('inf')] * n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if is_palindrome[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[n - 1]
