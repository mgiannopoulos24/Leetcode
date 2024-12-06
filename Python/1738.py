from typing import List
import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor = [[0] * n for _ in range(m)]
        values = []
        
        for i in range(m):
            for j in range(n):
                # Compute prefix XOR for the current cell
                current = matrix[i][j]
                if i > 0:
                    current ^= xor[i-1][j]
                if j > 0:
                    current ^= xor[i][j-1]
                if i > 0 and j > 0:
                    current ^= xor[i-1][j-1]
                xor[i][j] = current
                
                # Add to values list
                values.append(current)
        
        # Find the k-th largest element using a heap
        return heapq.nlargest(k, values)[-1]
