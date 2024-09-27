from typing import List

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # Helper class for Union-Find (Disjoint Set Union)
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.size = [1] * size

            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]  # Path compression
                    x = self.parent[x]
                return x

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX == rootY:
                    return
                # Union by size
                if self.size[rootX] < self.size[rootY]:
                    rootX, rootY = rootY, rootX
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

        m, n = len(grid), len(grid[0])
        # Copy the grid to apply the hits
        copy_grid = [row[:] for row in grid]
        for x, y in hits:
            # If there was a brick, remove it
            if copy_grid[x][y] == 1:
                copy_grid[x][y] = 0
            else:
                # Mark as -1 to indicate it was already empty
                copy_grid[x][y] = -1

        # Initialize Union-Find with an extra node for the top
        uf = UnionFind(m * n + 1)
        top = m * n  # Virtual top node

        # Function to convert 2D position to 1D
        def index(x, y):
            return x * n + y

        # Union the initial stable bricks
        for x in range(m):
            for y in range(n):
                if copy_grid[x][y] == 1:
                    if x == 0:
                        uf.union(index(x, y), top)
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and copy_grid[nx][ny] == 1:
                            uf.union(index(x, y), index(nx, ny))

        res = []
        # Process hits in reverse
        for x, y in reversed(hits):
            if grid[x][y] == 0:
                # It was already empty, no bricks fall
                res.append(0)
                continue
            # If the brick was originally empty, no effect
            if copy_grid[x][y] == -1:
                res.append(0)
                continue
            # Before adding the brick, record the current size connected to top
            prev_top = uf.size[uf.find(top)]
            # Restore the brick
            copy_grid[x][y] = 1
            # If the brick is in the first row, connect it to top
            if x == 0:
                uf.union(index(x, y), top)
            # Connect to adjacent bricks if they are present
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and copy_grid[nx][ny] == 1:
                    uf.union(index(x, y), index(nx, ny))
            # After adding, find the new size connected to top
            new_top = uf.size[uf.find(top)]
            # The number of bricks that became stable is the difference minus one (the restored brick itself)
            fallen = max(0, new_top - prev_top -1)
            res.append(fallen)

        # Since we processed hits in reverse, reverse the result before returning
        return res[::-1]
