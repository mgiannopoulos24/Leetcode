from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result list
        triangle = []
        
        for i in range(numRows):
            # Start a new row with 1's
            row = [1] * (i + 1)
            
            # Compute the values for the elements in between
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            # Add the row to the triangle
            triangle.append(row)
        
        return triangle
