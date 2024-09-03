class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        from collections import defaultdict
        import sys
        
        # Map to store the positions of each character in the ring
        char_positions = defaultdict(list)
        for index, char in enumerate(ring):
            char_positions[char].append(index)
        
        # Initialize DP table
        n = len(ring)
        m = len(key)
        dp = [[sys.maxsize] * n for _ in range(m)]
        
        # Base case
        for pos in char_positions[key[0]]:
            dp[0][pos] = min(pos, n - pos) + 1
        
        # Fill DP table
        for i in range(1, m):
            for j in char_positions[key[i]]:
                for k in char_positions[key[i-1]]:
                    diff = abs(j - k)
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(diff, n - diff) + 1)
        
        # Get the minimum steps for the last character of key
        return min(dp[m-1])
