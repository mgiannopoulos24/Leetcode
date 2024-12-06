class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words[0]), len(target)
        
        # Step 1: Build a frequency table for each character in each column of words
        freq = [[0] * 26 for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1
        
        # Step 2: dp[i] = number of ways to form the first i characters of target
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to form an empty target string
        
        # Step 3: For each column in words, update the dp array
        for j in range(m):
            # Update dp backwards to avoid overwriting information during this round
            for i in range(n - 1, -1, -1):
                char_idx = ord(target[i]) - ord('a')
                dp[i + 1] += dp[i] * freq[j][char_idx]
                dp[i + 1] %= MOD
        
        return dp[n]
