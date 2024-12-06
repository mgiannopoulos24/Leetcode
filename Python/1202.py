from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
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

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        
        # Apply union for all pairs
        for a, b in pairs:
            uf.union(a, b)
        
        # Group all characters by their connected component (i.e., root parent)
        groups = defaultdict(list)
        for i in range(n):
            root = uf.find(i)
            groups[root].append(s[i])
        
        # Sort each group's characters in lexicographical order
        for key in groups:
            groups[key].sort(reverse=True)
        
        # Rebuild the string using the smallest lexicographical character available in each group
        result = []
        for i in range(n):
            root = uf.find(i)
            result.append(groups[root].pop())
        
        return ''.join(result)
