class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Initialize a 2D array to keep track of champagne in each glass
        dp = [[0.0] * (i + 1) for i in range(101)]
        
        # Pour the champagne into the top glass
        dp[0][0] = poured
        
        # Process each row
        for i in range(100):
            for j in range(i + 1):
                # If the current glass has more than 1 cup of champagne
                if dp[i][j] > 1:
                    # Calculate excess champagne
                    excess = dp[i][j] - 1
                    # Distribute excess to the next row's adjacent glasses
                    dp[i + 1][j] += excess / 2
                    dp[i + 1][j + 1] += excess / 2
        
        # The amount of champagne in the target glass
        return min(1, dp[query_row][query_glass])
