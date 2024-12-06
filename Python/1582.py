class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Initialize the row and column sums
        row_sum = [sum(row) for row in mat]
        col_sum = [sum(col) for col in zip(*mat)]
        
        count = 0
        
        # Iterate over the matrix and check for special positions
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # Check if the position (i, j) is 1 and is a special position
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1
        
        return count
