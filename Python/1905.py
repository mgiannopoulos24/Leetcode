from typing import List, Tuple

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def flood_fill(grid: List[List[int]], i: int, j: int, cells: List[Tuple[int, int]]) -> None:
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                    grid[x][y] = -1  # Mark as visited
                    cells.append((x, y))
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        stack.append((x + dx, y + dy))
        
        def is_sub_island(cells_grid2: List[Tuple[int, int]]) -> bool:
            for x, y in cells_grid2:
                if not (0 <= x < len(grid1) and 0 <= y < len(grid1[0]) and grid1[x][y] == 1):
                    return False
            return True
        
        m, n = len(grid1), len(grid1[0])
        sub_island_count = 0
        
        # We use a copy of grid2 to mark visited cells
        visited_grid2 = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited_grid2[i][j]:
                    cells_grid2 = []
                    flood_fill(grid2, i, j, cells_grid2)
                    # Mark the cells as visited in grid2
                    for x, y in cells_grid2:
                        visited_grid2[x][y] = True
                    # Check if this island is a sub-island of grid1
                    if is_sub_island(cells_grid2):
                        sub_island_count += 1
        
        return sub_island_count
