class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Create a suffix sum array to make range sum calculations easier
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] + piles[i]
        
        # Memoization table
        memo = {}

        # Define the dp function
        def dp(i, M):
            # If we've taken all piles, no stones left to take
            if i == n:
                return 0
            
            # If result is already computed
            if (i, M) in memo:
                return memo[(i, M)]
            
            # If we take all remaining piles
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            # Try taking X piles, where 1 <= X <= 2 * M
            best = 0
            for x in range(1, 2 * M + 1):
                if i + x <= n:
                    # Calculate the remaining stones the opponent can leave us
                    best = max(best, suffix_sum[i] - dp(i + x, max(M, x)))
            
            memo[(i, M)] = best
            return best

        # Alice starts the game with M = 1
        return dp(0, 1)
