class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Sort the edges based on the distance
        edgeList.sort(key=lambda x: x[2])
        
        # Step 2: Sort the queries by limit, but keep track of the original indices
        queries_with_indices = [(p, q, limit, idx) for idx, (p, q, limit) in enumerate(queries)]
        queries_with_indices.sort(key=lambda x: x[2])
        
        # Step 3: Initialize Union-Find
        uf = UnionFind(n)
        answer = [False] * len(queries)
        edge_idx = 0
        
        # Step 4: Process each query in the sorted order
        for p, q, limit, query_idx in queries_with_indices:
            # Add all edges with distances < limit to the union-find
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, dist = edgeList[edge_idx]
                uf.union(u, v)
                edge_idx += 1
            
            # After processing edges, check if p and q are connected
            if uf.find(p) == uf.find(q):
                answer[query_idx] = True
        
        return answer
