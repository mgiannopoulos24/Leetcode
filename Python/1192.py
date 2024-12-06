from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        Finds all critical connections in the network using Tarjan's Algorithm.

        Args:
        n (int): Number of servers.
        connections (List[List[int]]): List of connections where each connection is [a, b].

        Returns:
        List[List[int]]: List of critical connections.
        """

        from collections import defaultdict

        # Step 1: Build the adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize necessary variables
        disc = [ -1 ] * n      # Discovery times of nodes
        low = [ -1 ] * n       # Low values of nodes
        bridges = []            # List to store bridges
        time = 0                # Global time counter

        def dfs(u: int, parent: int):
            nonlocal time
            disc[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if v == parent:
                    continue  # Skip the edge leading back to parent
                if disc[v] == -1:
                    # If v is not visited, recurse on it
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # If the lowest vertex reachable from v is
                    # after u in DFS tree, then u-v is a bridge
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                else:
                    # Update low[u] based on discovery time of v
                    low[u] = min(low[u], disc[v])

        # Step 2: Perform DFS from all unvisited nodes
        for i in range(n):
            if disc[i] == -1:
                dfs(i, -1)

        return bridges

