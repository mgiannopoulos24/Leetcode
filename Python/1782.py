from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * (n + 1)
        shared_edges = defaultdict(int)
        
        # Calculate degrees and shared edges
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1
            if u > v:
                u, v = v, u
            shared_edges[(u, v)] += 1

        # Sort degrees for efficient pair counting
        sorted_degrees = sorted(degree[1:])
        results = []
        
        for k in queries:
            # Count pairs with sum of degrees greater than k
            count = 0
            left, right = 0, n - 1
            
            while left < right:
                if sorted_degrees[left] + sorted_degrees[right] > k:
                    count += right - left
                    right -= 1
                else:
                    left += 1
            
            # Adjust count for shared edges
            for (u, v), shared in shared_edges.items():
                if degree[u] + degree[v] > k and degree[u] + degree[v] - shared <= k:
                    count -= 1
            
            results.append(count)
        
        return results
