from typing import List
from heapq import heappop, heappush
from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the graph using an adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Step 2: Calculate shortest paths to node n using Dijkstra's algorithm
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        min_heap = [(0, n)]  # (distance, node)

        while min_heap:
            d, node = heappop(min_heap)
            if d > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heappush(min_heap, (new_dist, neighbor))

        # Step 3: Count restricted paths using DFS with memoization
        memo = {}

        def dfs(node):
            if node == n:
                return 1
            if node in memo:
                return memo[node]

            path_count = 0
            for neighbor, weight in graph[node]:
                if dist[node] > dist[neighbor]:  # Only go to neighbors closer to node n
                    path_count += dfs(neighbor)
                    path_count %= MOD

            memo[node] = path_count
            return path_count

        # Start DFS from node 1
        return dfs(1)
