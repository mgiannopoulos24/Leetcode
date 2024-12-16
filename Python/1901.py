from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        
        # Binary search on columns
        left, right = 0, n - 1
        
        while left <= right:
            mid_col = (left + right) // 2
            # Find the row with the maximum element in the mid column
            max_row = 0
            for i in range(m):
                if mat[i][mid_col] > mat[max_row][mid_col]:
                    max_row = i
            
            # Check if the current element is a peak
            # Compare the element with its left and right neighbors
            if (mid_col == 0 or mat[max_row][mid_col] > mat[max_row][mid_col - 1]) and \
               (mid_col == n - 1 or mat[max_row][mid_col] > mat[max_row][mid_col + 1]):
                return [max_row, mid_col]
            elif mid_col > 0 and mat[max_row][mid_col - 1] > mat[max_row][mid_col]:
                # If the left neighbor is larger, move left
                right = mid_col - 1
            else:
                # If the right neighbor is larger, move right
                left = mid_col + 1
