from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # Get the dimensions of the matrix
        m, n = len(rowSum), len(colSum)
        
        # Initialize the result matrix with zeros
        matrix = [[0] * n for _ in range(m)]
        
        # Iterate through each row and column, filling the matrix
        for i in range(m):
            for j in range(n):
                # Assign the minimum possible value to the cell (i, j)
                value = min(rowSum[i], colSum[j])
                matrix[i][j] = value
                
                # Update the rowSum and colSum by subtracting the value
                rowSum[i] -= value
                colSum[j] -= value
        
        return matrix
