class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Number of rows and columns
        rows = len(grid)
        cols = len(grid[0])
        
        # Start from the bottom-left corner
        row = rows - 1
        col = 0
        count = 0
        
        # Move within the grid
        while row >= 0 and col < cols:
            if grid[row][col] < 0:
                # All elements to the right of this element in the row are negative
                count += (cols - col)
                # Move up to the previous row
                row -= 1
            else:
                # Move right to the next column
                col += 1
        
        return count
