from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Get the number of rows and columns
        rows, cols = len(matrix), len(matrix[0])
        
        # Compute the prefix sum for each row
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c-1]
        
        count = 0
        
        # Iterate over all pairs of columns
        for col_start in range(cols):
            for col_end in range(col_start, cols):
                subarray_sum = defaultdict(int)
                subarray_sum[0] = 1  # Handle the case where submatrix sum is exactly the target
                curr_sum = 0
                
                # Iterate through each row, treating the sum between col_start and col_end as a subarray
                for r in range(rows):
                    # Compute the sum of the subarray for the current row
                    if col_start > 0:
                        curr_sum += matrix[r][col_end] - matrix[r][col_start - 1]
                    else:
                        curr_sum += matrix[r][col_end]
                    
                    # Check if we have seen (curr_sum - target) before, which means there is a valid submatrix
                    count += subarray_sum[curr_sum - target]
                    
                    # Record the current prefix sum
                    subarray_sum[curr_sum] += 1
        
        return count
