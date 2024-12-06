class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # DP arrays to store the number of continuous 1's to the left and up of each cell
        horiz = [[0] * cols for _ in range(rows)]
        vert = [[0] * cols for _ in range(rows)]
        
        # Fill the DP arrays
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    horiz[i][j] = horiz[i][j-1] + 1 if j > 0 else 1
                    vert[i][j] = vert[i-1][j] + 1 if i > 0 else 1
        
        max_side = 0
        
        # Iterate through all possible bottom-right corners of squares
        for i in range(rows):
            for j in range(cols):
                # Try different square sizes, starting from the largest
                for side in range(min(horiz[i][j], vert[i][j]), 0, -1):
                    if i - side + 1 >= 0 and j - side + 1 >= 0:
                        if horiz[i - side + 1][j] >= side and vert[i][j - side + 1] >= side:
                            max_side = max(max_side, side)
                            break  # No need to try smaller squares for this cell
        
        return max_side * max_side
