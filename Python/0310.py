from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # Initialize the graph
        adjacency_list = [[] for _ in range(n)]
        degree = [0] * n
        
        # Build the graph
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
            degree[a] += 1
            degree[b] += 1
            
        # Initialize the first layer of leaves
        leaves = deque([i for i in range(n) if degree[i] == 1])
        
        # Remove leaves layer by layer
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adjacency_list[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        
        # The remaining nodes are the centroids of the graph
        return list(leaves)