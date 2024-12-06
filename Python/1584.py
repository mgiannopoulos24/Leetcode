import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Calculate the number of points
        n = len(points)
        
        # Create a min-heap (priority queue) for Prim's algorithm
        heap = [(0, 0)]  # (cost, point_index) start with the first point
        in_mst = [False] * n  # To keep track of points already in the MST
        total_cost = 0
        edges_used = 0
        
        while edges_used < n:
            # Get the point with the smallest cost to add to the MST
            cost, u = heapq.heappop(heap)
            
            # If the point is already in the MST, skip it
            if in_mst[u]:
                continue
            
            # Add the cost to the total cost and mark this point as part of the MST
            total_cost += cost
            in_mst[u] = True
            edges_used += 1
            
            # For each point, calculate the cost to connect it to the current point
            for v in range(n):
                if not in_mst[v]:
                    # Manhattan distance between points u and v
                    manhattan_distance = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (manhattan_distance, v))
        
        return total_cost
