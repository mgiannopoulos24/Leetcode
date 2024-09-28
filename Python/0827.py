class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        from collections import defaultdict

        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def in_bounds(x, y):
            return 0 <= x < n and 0 <= y < n
        
        def dfs(x, y, island_id):
            stack = [(x, y)]
            size = 0
            while stack:
                cx, cy = stack.pop()
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))
                island_map[cx][cy] = island_id
                size += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if in_bounds(nx, ny) and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        stack.append((nx, ny))
            return size
        
        island_map = [[0] * n for _ in range(n)]
        island_sizes = {}
        island_id = 0
        
        visited = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1
        
        max_island_size = max(island_sizes.values(), default=0)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    adjacent_islands = set()
                    current_size = 1  # The current `0` turned into `1`
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy
                        if in_bounds(nx, ny) and grid[nx][ny] == 1:
                            island = island_map[nx][ny]
                            if island not in adjacent_islands:
                                adjacent_islands.add(island)
                                current_size += island_sizes[island]
                    max_island_size = max(max_island_size, current_size)
        
        return max_island_size
