from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify matrix in-place to set entire rows and columns to zero if any element is zero.
        """
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Determine if the first row and first column need to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and column to mark zeroes for rest of the matrix
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the first column of this row
                    matrix[0][j] = 0  # Mark the first row of this column
        
        # Zero out the cells based on marks in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Zero out the first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0