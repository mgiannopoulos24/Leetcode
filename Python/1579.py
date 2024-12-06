from typing import List

class DSU:
    def __init__(self, n):
        # Parent array
        self.parent = list(range(n + 1))
        # Rank array for optimization
        self.rank = [0] * (n + 1)
        # Initially, number of connected components is n
        self.components = n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Union by rank
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False  # No union performed, already connected
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        self.components -= 1
        return True  # Union performed

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Sort edges so that Type 3 edges are processed first
        edges.sort(reverse=True, key=lambda x: x[0])

        alice_dsu = DSU(n)
        bob_dsu = DSU(n)
        removed = 0

        for edge in edges:
            type_, u, v = edge
            if type_ == 3:
                # Attempt to unify for both Alice and Bob
                alice_union = alice_dsu.union(u, v)
                bob_union = bob_dsu.union(u, v)
                if not alice_union and not bob_union:
                    # Edge is redundant for both
                    removed += 1
            elif type_ == 1:
                # Only Alice can use this edge
                if not alice_dsu.union(u, v):
                    # Edge is redundant for Alice
                    removed += 1
            elif type_ == 2:
                # Only Bob can use this edge
                if not bob_dsu.union(u, v):
                    # Edge is redundant for Bob
                    removed += 1

        # After processing all edges, check if both Alice and Bob can traverse the entire graph
        if alice_dsu.components != 1 or bob_dsu.components != 1:
            return -1

        return removed
