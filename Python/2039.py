from collections import deque, defaultdict

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        n = len(patience)
        graph = defaultdict(list)
        
        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # BFS to find the shortest distance from each node to the master server (0)
        distance = [0] * n
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + 1
                    queue.append(neighbor)
        
        # Calculate the time when the network becomes idle
        max_time = 0
        for i in range(1, n):
            round_trip_time = 2 * distance[i]
            last_send = (round_trip_time - 1) // patience[i] * patience[i]
            last_reply = last_send + round_trip_time
            max_time = max(max_time, last_reply)
        
        return max_time + 1  # The network becomes idle at the beginning of the next second