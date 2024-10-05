class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = size  # Total number of components
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
    
    def get_count(self):
        return self.count


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # Each cell is divided into 4 regions, so the grid has 4 * n * n regions.
        uf = UnionFind(4 * n * n)
        
        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)  # Index of the current cell's top-left region
                
                # Union regions within the current cell
                if grid[i][j] == '/':
                    # '/' connects region 0 and 3, and region 1 and 2
                    uf.union(index + 0, index + 3)
                    uf.union(index + 1, index + 2)
                elif grid[i][j] == '\\':
                    # '\' connects region 0 and 1, and region 2 and 3
                    uf.union(index + 0, index + 1)
                    uf.union(index + 2, index + 3)
                else:
                    # ' ' connects all 4 regions in the cell
                    uf.union(index + 0, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)
                
                # Union between adjacent cells
                # Connect right neighbor (current cell's region 1 with right cell's region 3)
                if j + 1 < n:
                    right_index = 4 * (i * n + j + 1)
                    uf.union(index + 1, right_index + 3)
                
                # Connect bottom neighbor (current cell's region 2 with bottom cell's region 0)
                if i + 1 < n:
                    bottom_index = 4 * ((i + 1) * n + j)
                    uf.union(index + 2, bottom_index + 0)
        
        return uf.get_count()
