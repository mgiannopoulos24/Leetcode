class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Number of rows in the original matrix
        m = len(matrix)
        # Number of columns in the original matrix
        n = len(matrix[0])
        
        # Initialize the transposed matrix with dimensions n x m
        transpose = [[0] * m for _ in range(n)]
        
        # Fill the transpose matrix
        for i in range(m):
            for j in range(n):
                transpose[j][i] = matrix[i][j]
        
        return transpose
