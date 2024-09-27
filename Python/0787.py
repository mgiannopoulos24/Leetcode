from typing import List
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize the distance array with infinity
        dist = [math.inf] * n
        dist[src] = 0
        
        # Process up to k+1 stops
        for _ in range(k + 1):
            # Create a copy of the distance array for this iteration
            temp_dist = dist[:]
            for u, v, w in flights:
                if dist[u] != math.inf:
                    temp_dist[v] = min(temp_dist[v], dist[u] + w)
            # Update the distance array
            dist = temp_dist
        
        # The result is the distance to the destination city
        return dist[dst] if dist[dst] != math.inf else -1
