from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # Check if reshape is possible
        if m * n != r * c:
            return mat
        
        # Flatten the matrix
        flat_list = [num for row in mat for num in row]
        
        # Create the reshaped matrix
        reshaped_matrix = []
        for i in range(r):
            reshaped_matrix.append(flat_list[i*c:(i+1)*c])
        
        return reshaped_matrix
