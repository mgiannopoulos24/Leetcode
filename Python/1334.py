class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Step 1: Initialize the distance matrix
        inf = float('inf')
        dist = [[inf] * n for _ in range(n)]
        
        # Step 2: Set distance for each city to itself to 0
        for i in range(n):
            dist[i][i] = 0
        
        # Step 3: Set the distances based on the given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Step 4: Apply Floyd-Warshall to find all pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Step 5: Count reachable cities within the distanceThreshold for each city
        result_city = -1
        min_reachable = n  # We aim to minimize this
        for i in range(n):
            count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            
            # Step 6: Choose the city with the smallest number of reachable cities
            # If there's a tie, prefer the city with the largest index
            if count <= min_reachable:
                min_reachable = count
                result_city = i
        
        return result_city
