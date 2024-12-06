from collections import defaultdict, deque

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegree = [0] * n
        graph = defaultdict(list)

        # Build the graph and indegree array
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Topological sorting using Kahn's algorithm
        queue = deque([i for i in range(n) if indegree[i] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Check for cycles
        if len(topo_order) != n:
            return -1

        # DP to calculate the largest color value
        dp = [[0] * 26 for _ in range(n)]
        max_color_value = 0

        for node in topo_order:
            color_idx = ord(colors[node]) - ord('a')
            dp[node][color_idx] += 1
            max_color_value = max(max_color_value, dp[node][color_idx])

            for neighbor in graph[node]:
                for c in range(26):
                    dp[neighbor][c] = max(dp[neighbor][c], dp[node][c])

        return max_color_value
