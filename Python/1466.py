from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Graph representation
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        # Build the graph where (u -> v) means road is directed from u to v
        for u, v in connections:
            graph[u].append(v)  # Road goes from u to v
            reverse_graph[v].append(u)  # Road goes from v to u (reaching city 0 from this direction)

        changes = 0
        visited = [False] * n
        queue = deque([0])  # Start BFS from city 0
        
        while queue:
            city = queue.popleft()
            visited[city] = True

            # Explore roads that are directed away from the current city
            for neighbor in graph[city]:
                if not visited[neighbor]:
                    changes += 1  # This road needs to be reversed
                    queue.append(neighbor)

            # Explore roads that are directed towards the current city
            for neighbor in reverse_graph[city]:
                if not visited[neighbor]:
                    queue.append(neighbor)

        return changes
