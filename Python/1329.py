class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # Dictionary to store elements of each diagonal
        diagonals = {}
        
        # Collect all elements belonging to each diagonal
        for r in range(m):
            for c in range(n):
                diag_key = r - c
                if diag_key not in diagonals:
                    diagonals[diag_key] = []
                diagonals[diag_key].append(mat[r][c])
        
        # Sort each diagonal
        for key in diagonals:
            diagonals[key].sort(reverse=True)  # Sort in descending order so we can pop from the end
        
        # Place sorted elements back into the matrix
        for r in range(m):
            for c in range(n):
                diag_key = r - c
                mat[r][c] = diagonals[diag_key].pop()  # Pop the smallest element and place it in the matrix
        
        return mat
