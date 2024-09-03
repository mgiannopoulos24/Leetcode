from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        # A helper function to collect diagonal elements
        def collect_diagonal(diagonal_index: int):
            if diagonal_index % 2 == 0:
                # Collect from bottom-left to top-right
                r = min(diagonal_index, m - 1)
                c = diagonal_index - r
                while r >= 0 and c < n:
                    result.append(mat[r][c])
                    r -= 1
                    c += 1
            else:
                # Collect from top-right to bottom-left
                c = min(diagonal_index, n - 1)
                r = diagonal_index - c
                while c >= 0 and r < m:
                    result.append(mat[r][c])
                    r += 1
                    c -= 1
        
        # Collect all diagonals
        for diag in range(m + n - 1):
            collect_diagonal(diag)
        
        return result
