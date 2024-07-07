from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            h = min(height[left], height[right])
            width = right - left
            current_area = h * width
            
            # Update max_area if current_area is larger
            if current_area > max_area:
                max_area = current_area
            
            # Move pointers based on which pointer points to shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area