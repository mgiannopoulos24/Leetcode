from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2  # Number of layers
        
        for layer in range(layers):
            # Extract the current layer
            elements = []
            
            # Top row (left to right)
            for col in range(layer, n - layer):
                elements.append(grid[layer][col])
            
            # Right column (top to bottom)
            for row in range(layer + 1, m - layer):
                elements.append(grid[row][n - layer - 1])
            
            # Bottom row (right to left)
            for col in range(n - layer - 2, layer - 1, -1):
                elements.append(grid[m - layer - 1][col])
            
            # Left column (bottom to top)
            for row in range(m - layer - 2, layer, -1):
                elements.append(grid[row][layer])
            
            # Rotate the layer
            length = len(elements)
            k_mod = k % length
            rotated = elements[k_mod:] + elements[:k_mod]
            
            # Reassign the rotated elements back to the grid
            idx = 0
            
            # Top row (left to right)
            for col in range(layer, n - layer):
                grid[layer][col] = rotated[idx]
                idx += 1
            
            # Right column (top to bottom)
            for row in range(layer + 1, m - layer):
                grid[row][n - layer - 1] = rotated[idx]
                idx += 1
            
            # Bottom row (right to left)
            for col in range(n - layer - 2, layer - 1, -1):
                grid[m - layer - 1][col] = rotated[idx]
                idx += 1
            
            # Left column (bottom to top)
            for row in range(m - layer - 2, layer, -1):
                grid[row][layer] = rotated[idx]
                idx += 1
        
        return grid
