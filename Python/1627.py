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

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # Union-Find structure for cities from 1 to n (0-indexed, so need n+1)
        uf = UnionFind(n + 1)
        
        # Connect cities with a common divisor greater than threshold
        for divisor in range(threshold + 1, n + 1):
            for multiple in range(2 * divisor, n + 1, divisor):
                uf.union(divisor, multiple)
        
        # Answer the queries
        result = []
        for a, b in queries:
            if uf.find(a) == uf.find(b):
                result.append(True)
            else:
                result.append(False)
        
        return result
