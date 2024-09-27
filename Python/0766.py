from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return True
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Check diagonals starting from each element in the first row
        for j in range(n):
            value = matrix[0][j]
            x, y = 0, j
            while x < m and y < n:
                if matrix[x][y] != value:
                    return False
                x += 1
                y += 1
        
        # Check diagonals starting from each element in the first column
        for i in range(1, m):
            value = matrix[i][0]
            x, y = i, 0
            while x < m and y < n:
                if matrix[x][y] != value:
                    return False
                x += 1
                y += 1
        
        return True
