class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(pizza), len(pizza[0])

        # Step 1: Create a 2D prefix sum array to store the number of apples in the submatrix (i,j) -> (rows-1, cols-1)
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = (1 if pizza[r][c] == 'A' else 0) + apples[r+1][c] + apples[r][c+1] - apples[r+1][c+1]
        
        # Step 2: DP table to store the number of ways to cut pizza from (r, c) with `c` cuts left
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
        
        # Base case: If we need to make 0 more cuts, there's 1 way if the current piece contains an apple
        for r in range(rows):
            for c in range(cols):
                if apples[r][c] > 0:  # There's at least one apple in the remaining piece
                    dp[r][c][0] = 1
        
        # Step 3: Fill DP table for cases where we need `c` cuts
        for cuts in range(1, k):
            for r in range(rows):
                for c in range(cols):
                    # Try horizontal cuts
                    for nr in range(r + 1, rows):
                        if apples[r][c] - apples[nr][c] > 0:  # There's at least one apple in the top part
                            dp[r][c][cuts] = (dp[r][c][cuts] + dp[nr][c][cuts - 1]) % MOD
                    
                    # Try vertical cuts
                    for nc in range(c + 1, cols):
                        if apples[r][c] - apples[r][nc] > 0:  # There's at least one apple in the left part
                            dp[r][c][cuts] = (dp[r][c][cuts] + dp[r][nc][cuts - 1]) % MOD
        
        # Step 4: The result is the number of ways to cut the whole pizza into `k` pieces
        return dp[0][0][k - 1]

