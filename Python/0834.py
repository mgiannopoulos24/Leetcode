from typing import List
from collections import defaultdict

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build the adjacency list representation of the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize data structures
        subtree_size = [0] * n
        distance_sum = [0] * n
        visited = [False] * n
        
        # First DFS to calculate subtree sizes and initial distances from node 0
        def dfs1(node: int) -> None:
            visited[node] = True
            subtree_size[node] = 1
            total_distance = 0
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs1(neighbor)
                    subtree_size[node] += subtree_size[neighbor]
                    total_distance += distance_sum[neighbor] + subtree_size[neighbor]
            distance_sum[node] = total_distance
        
        # Second DFS to calculate distances for all nodes based on root's distances
        def dfs2(node: int) -> None:
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    # Before visiting the neighbor, adjust its distance_sum
                    distance_sum[neighbor] = (distance_sum[node] 
                                              - subtree_size[neighbor] 
                                              + (n - subtree_size[neighbor]))
                    dfs2(neighbor)
        
        # Run the first DFS from node 0
        dfs1(0)
        
        # Reset visited array for the second DFS
        visited = [False] * n
        
        # Run the second DFS from node 0
        dfs2(0)
        
        return distance_sum
