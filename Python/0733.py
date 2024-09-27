from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Get the dimensions of the image
        m, n = len(image), len(image[0])
        
        # The original color of the starting pixel
        original_color = image[sr][sc]
        
        # If the original color is the same as the new color, no need to do anything
        if original_color == color:
            return image
        
        # Define directions for 4-connected neighbors (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Initialize the stack with the starting pixel
        stack = [(sr, sc)]
        
        while stack:
            r, c = stack.pop()
            # Color the current pixel
            image[r][c] = color
            
            # Explore all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check if the neighbor is within bounds and has the original color
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original_color:
                    stack.append((nr, nc))
        
        return image
