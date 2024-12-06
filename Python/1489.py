class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Attach index to each edge to keep track of original positions
        for i in range(len(edges)):
            edges[i].append(i)

        # Step 2: Sort the edges by their weight
        edges.sort(key=lambda x: x[2])

        # Helper function to find the MST weight using Kruskal's algorithm
        def kruskal(n, edges, skip_edge=-1, force_edge=-1):
            uf = UnionFind(n)
            mst_weight = 0
            edges_used = 0

            # Force add the forced edge
            if force_edge != -1:
                u, v, w, _ = edges[force_edge]
                if uf.union(u, v):
                    mst_weight += w
                    edges_used += 1

            # Normal Kruskal's algorithm
            for i, (u, v, w, _) in enumerate(edges):
                if i == skip_edge:
                    continue
                if uf.union(u, v):
                    mst_weight += w
                    edges_used += 1
                if edges_used == n - 1:
                    break

            # If we don't have n - 1 edges in the MST, it's invalid
            return mst_weight if edges_used == n - 1 else float('inf')

        # Step 3: Calculate the total weight of the MST without any modifications
        original_mst_weight = kruskal(n, edges)

        critical = []
        pseudo_critical = []

        # Step 4: Check each edge
        for i, edge in enumerate(edges):
            # Check if it's a critical edge
            if kruskal(n, edges, skip_edge=i) > original_mst_weight:
                critical.append(edge[3])
            # Check if it's a pseudo-critical edge
            elif kruskal(n, edges, force_edge=i) == original_mst_weight:
                pseudo_critical.append(edge[3])

        return [critical, pseudo_critical]
