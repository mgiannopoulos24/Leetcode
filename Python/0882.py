import heapq
from typing import List

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """
        Determines the number of nodes reachable from node 0 in a subdivided graph within maxMoves.

        :param edges: List of edges in the original graph, where each edge is represented as [u, v, cnt].
        :param maxMoves: Maximum number of moves allowed.
        :param n: Number of nodes in the original graph.
        :return: Total number of reachable nodes (original and subdivided).
        """
        
        # Step 1: Build the adjacency list with effective distances (cnt + 1)
        adj = [[] for _ in range(n)]
        for u, v, cnt in edges:
            adj[u].append( (v, cnt + 1) )  # Edge weight is cnt + 1
            adj[v].append( (u, cnt + 1) )
        
        # Step 2: Initialize distances and the priority queue for Dijkstra's algorithm
        distances = [float('inf')] * n
        distances[0] = 0
        heap = [ (0, 0) ]  # (distance, node)
        
        while heap:
            current_distance, u = heapq.heappop(heap)
            
            # If we have already found a better path, skip
            if current_distance > distances[u]:
                continue
            
            # Explore neighbors
            for v, weight in adj[u]:
                if current_distance + weight < distances[v]:
                    distances[v] = current_distance + weight
                    heapq.heappush(heap, (distances[v], v))
        
        # Step 3: Count reachable original nodes
        reachable_original = sum(1 for d in distances if d <= maxMoves)
        
        # Step 4: Count reachable subdivided nodes
        reachable_new = 0
        for u, v, cnt in edges:
            # Calculate reachable subdivided nodes from both ends
            # left = number of new nodes reachable from u
            left = maxMoves - distances[u]
            left = left if left > 0 else 0
            left = min(cnt, left)
            
            # right = number of new nodes reachable from v
            right = maxMoves - distances[v]
            right = right if right > 0 else 0
            right = min(cnt, right)
            
            # Total reachable new nodes on this edge is min(cnt, left + right)
            reachable_new += min(cnt, left + right)
        
        # Step 5: Return the total reachable nodes
        return reachable_original + reachable_new
