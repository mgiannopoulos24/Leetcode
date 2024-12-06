from typing import List
from collections import defaultdict
import math

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # Precompute the coprimality lookup table for numbers 1 to 50
        max_val = 50
        coprime = [[math.gcd(i, j) == 1 for j in range(max_val + 1)] for i in range(max_val + 1)]
        
        # Build the graph (tree) from edges
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize the result array and last_seen dictionary
        ans = [-1] * n
        last_seen = defaultdict(list)  # Maps value to (depth, node) tuples for closest ancestors

        # DFS function
        def dfs(node, parent, depth):
            closest_ancestor = -1
            min_depth = -1
            
            # Check for the closest coprime ancestor
            for val in range(1, max_val + 1):
                if coprime[nums[node]][val] and last_seen[val]:
                    last_depth, last_node = last_seen[val][-1]
                    # Update closest ancestor if it's the deepest valid coprime
                    if min_depth == -1 or last_depth > min_depth:
                        closest_ancestor = last_node
                        min_depth = last_depth
            
            # Record the closest coprime ancestor for this node
            ans[node] = closest_ancestor
            
            # Update the last_seen list for this node's value
            last_seen[nums[node]].append((depth, node))
            
            # Visit all children (DFS)
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1)
            
            # Backtrack: remove the current node from last_seen to keep only relevant ancestors
            last_seen[nums[node]].pop()

        # Start DFS from the root node (node 0)
        dfs(0, -1, 0)
        
        return ans
