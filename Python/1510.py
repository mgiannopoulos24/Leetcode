class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] will be True if the player to move can win with i stones remaining
        dp = [False] * (n + 1)
        
        # Iterate over all possible stone counts from 1 to n
        for i in range(1, n + 1):
            # Try all possible square numbers that can be removed
            j = 1
            while j * j <= i:
                # If removing a square number j*j leaves the opponent in a losing position (dp[i - j*j] == False),
                # then the current player can win with i stones.
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1
        
        # Return whether the player can win with n stones
        return dp[n]
