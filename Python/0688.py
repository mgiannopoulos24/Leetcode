class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible knight moves
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        # DP table: dp[m][r][c] is the probability of being at (r, c) after m moves
        dp = [[[0.0] * n for _ in range(n)] for _ in range(k + 1)]
        
        # Initial position has probability 1 with 0 moves
        dp[0][row][column] = 1.0
        
        # Fill the DP table
        for move in range(k):
            for r in range(n):
                for c in range(n):
                    if dp[move][r][c] > 0:
                        for dr, dc in moves:
                            new_r, new_c = r + dr, c + dc
                            if 0 <= new_r < n and 0 <= new_c < n:
                                dp[move + 1][new_r][new_c] += dp[move][r][c] / 8.0
        
        # Sum up probabilities of being on the board after k moves
        probability = sum(dp[k][r][c] for r in range(n) for c in range(n))
        
        return probability
