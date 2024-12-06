from collections import defaultdict, deque

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)
        
        # Step 2: Helper function to check if a set of nodes is connected
        def is_connected(subset):
            # Find the first node in the subset
            nodes = [i for i in range(n) if subset & (1 << i)]
            if not nodes:
                return False
            
            # Use BFS/DFS to check if all nodes in the subset are connected
            visited = set()
            queue = deque([nodes[0]])
            visited.add(nodes[0])
            
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor not in visited and (subset & (1 << neighbor)):
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            return len(visited) == len(nodes)
        
        # Step 3: Helper function to compute the diameter of a connected component
        def bfs_longest_path(start, subset):
            # BFS to find the farthest node from 'start'
            queue = deque([start])
            dist = {start: 0}
            farthest_node = start
            
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor not in dist and (subset & (1 << neighbor)):
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
                        if dist[neighbor] > dist[farthest_node]:
                            farthest_node = neighbor
            
            return farthest_node, dist[farthest_node]
        
        # Step 4: Calculate the number of subtrees with a given diameter
        result = [0] * (n - 1)
        
        for subset in range(1, 1 << n):
            if is_connected(subset):
                # Find the farthest node from an arbitrary node in the subset
                first_node = [i for i in range(n) if subset & (1 << i)][0]
                u, _ = bfs_longest_path(first_node, subset)
                v, diameter = bfs_longest_path(u, subset)
                
                if diameter > 0:
                    result[diameter - 1] += 1
        
        return result
