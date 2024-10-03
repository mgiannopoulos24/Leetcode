from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        # Process each row from bottom to top
        for i in range(n - 2, -1, -1):
            for j in range(n):
                # Minimum value of the cell directly below
                min_below = matrix[i + 1][j]
                
                # Check diagonally left
                if j > 0:
                    min_below = min(min_below, matrix[i + 1][j - 1])
                
                # Check diagonally right
                if j < n - 1:
                    min_below = min(min_below, matrix[i + 1][j + 1])
                
                # Update the current cell with the minimum path sum
                matrix[i][j] += min_below
        
        # The answer is the minimum value in the top row
        return min(matrix[0])
