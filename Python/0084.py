from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack to keep indices of the bars in the histogram
        stack = []
        max_area = 0
        index = 0
        
        while index < len(heights):
            # Push the current index if the current bar is taller than the bar at the stack's top
            if not stack or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                # Calculate the area with the bar at the top of the stack as the shortest bar
                top_of_stack = stack.pop()
                height = heights[top_of_stack]
                width = index if not stack else index - stack[-1] - 1
                max_area = max(max_area, height * width)
        
        # Now pop the remaining bars in the stack and calculate the area
        while stack:
            top_of_stack = stack.pop()
            height = heights[top_of_stack]
            width = index if not stack else index - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area