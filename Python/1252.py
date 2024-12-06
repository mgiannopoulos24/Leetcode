class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Arrays to track how many times each row and column is incremented
        row_incr = [0] * m
        col_incr = [0] * n
        
        # Apply increments based on indices
        for r, c in indices:
            row_incr[r] += 1
            col_incr[c] += 1
        
        # Count the number of odd cells
        odd_count = 0
        for i in range(m):
            for j in range(n):
                # A cell (i, j) is odd if row_incr[i] + col_incr[j] is odd
                if (row_incr[i] + col_incr[j]) % 2 == 1:
                    odd_count += 1
        
        return odd_count
