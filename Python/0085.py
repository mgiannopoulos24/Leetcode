from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        # Dimensions of the matrix
        rows, cols = len(matrix), len(matrix[0])
        
        # Heights array to store the heights of histogram
        heights = [0] * cols
        max_area = 0
        
        for i in range(rows):
            for j in range(cols):
                # Update the heights array
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            # Calculate the maximum area with the current row as the base of the histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This function is used to calculate the largest rectangle in the histogram
        stack = []
        max_area = 0
        heights.append(0)  # Add a 0 height to handle remaining bars
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        heights.pop()  # Remove the appended 0 height
        return max_area