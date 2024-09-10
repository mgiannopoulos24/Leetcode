class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Helper class for Union-Find
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
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
                    return True
                return False
        
        n = len(edges)
        uf = UnionFind(n + 1)  # 1-based indexing
        
        # Iterate over each edge
        for u, v in edges:
            if not uf.union(u, v):
                # If union returns False, it means u and v are already connected, indicating a cycle.
                return [u, v]
