from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create the adjacency list
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Initialize the distance array and priority queue
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        min_heap = [(0, k)]  # (distance, node)
        
        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
            
            # Early exit if the current distance is greater than the recorded distance
            if current_dist > dist[u]:
                continue
            
            # Explore neighbors
            for v, w in graph[u]:
                new_dist = current_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))
        
        # Find the maximum distance among all nodes
        max_dist = max(dist[1:])
        
        # If any node is unreachable, return -1
        return max_dist if max_dist < float('inf') else -1
