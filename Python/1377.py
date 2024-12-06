from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # BFS setup
        queue = deque([(1, 1.0, 0)])  # (current_node, probability, time)
        visited = set([1])  # Start from vertex 1
        
        while queue:
            node, prob, time = queue.popleft()
            
            # If we reach the target and time is not exceeded, return the probability
            if node == target:
                # If the frog is at the target and either it's a leaf node or no more time left
                if time == t or (len(tree[node]) == (1 if node != 1 else 0)):  # Leaf node case
                    return prob
                return 0.0  # If frog can still jump but time isn't enough to reach t
            
            # If time exceeds allowed limit, we can't proceed further
            if time >= t:
                continue
            
            # Count the number of unvisited neighbors (potential next jumps)
            unvisited_neighbors = [neighbor for neighbor in tree[node] if neighbor not in visited]
            if not unvisited_neighbors:
                continue  # No valid neighbors to jump to
            
            # Spread probability equally among all unvisited neighbors
            next_prob = prob / len(unvisited_neighbors)
            
            # Enqueue the neighbors for BFS
            for neighbor in unvisited_neighbors:
                visited.add(neighbor)
                queue.append((neighbor, next_prob, time + 1))
        
        return 0.0  # If we exhaust all possibilities without reaching target
