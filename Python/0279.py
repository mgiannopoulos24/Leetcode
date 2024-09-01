class Solution:
    def numSquares(self, n: int) -> int:
        # List to store the minimum number of perfect squares for each number
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: zero perfect squares are needed to sum up to 0
        
        # Precompute all perfect squares less than or equal to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        # Fill the dp array
        for i in range(1, n + 1):
            for square in squares:
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]
