import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create the graph as an adjacency list
        graph = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Max-heap (priority queue) with negative probabilities for max-heap simulation
        max_heap = [(-1.0, start_node)]  # (negative probability, node)
        max_prob = [0] * n
        max_prob[start_node] = 1.0
        
        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob  # Convert back to positive probability
            
            if node == end_node:
                return current_prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = current_prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        return 0.0
