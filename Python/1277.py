class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # Get the dimensions of the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create a dp table with the same dimensions as the matrix
        dp = [[0] * cols for _ in range(rows)]
        
        # Variable to store the total count of square submatrices
        total_squares = 0
        
        # Fill the dp table
        for i in range(rows):
            for j in range(cols):
                # If it's a 1 and it's not in the first row or first column
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # First row or column can only form size 1 squares
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                # Add the count of squares ending at this cell
                total_squares += dp[i][j]
        
        return total_squares
