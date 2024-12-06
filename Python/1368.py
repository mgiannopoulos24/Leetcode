import heapq

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # Define the dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Direction vectors for [right, left, down, up]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Priority queue for Dijkstra-like exploration (cost, row, col)
        pq = [(0, 0, 0)]  # (cost, row, col) starting at (0, 0) with cost 0
        
        # Distance matrix to store the minimum cost to reach each cell
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        while pq:
            cost, r, c = heapq.heappop(pq)
            
            # If we reached the bottom-right corner, return the cost
            if r == m - 1 and c == n - 1:
                return cost
            
            # If the current cost is greater than what we have in dist, skip this path
            if cost > dist[r][c]:
                continue
            
            # Explore the 4 possible directions (right, left, down, up)
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc  # Next row and column
                
                # Check if it's within bounds
                if 0 <= nr < m and 0 <= nc < n:
                    # If the direction matches the current grid value, cost is 0
                    new_cost = cost if grid[r][c] == i + 1 else cost + 1
                    
                    # If a cheaper path is found, update the distance and push to pq
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
        
        # The bottom-right corner will always be reached, so no need to return anything here.
