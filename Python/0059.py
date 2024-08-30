from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Initialize the matrix with zeroes
        matrix = [[0] * n for _ in range(n)]
        
        # Define the boundaries of the matrix
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1  # Start with the number 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # Traverse from right to left along the bottom boundary
            if top <= bottom:  # Check to avoid duplicate rows
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            
            # Traverse from bottom to top along the left boundary
            if left <= right:  # Check to avoid duplicate columns
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix
