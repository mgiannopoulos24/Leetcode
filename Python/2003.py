from typing import List
from collections import defaultdict

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        n = len(parents)
        ans = [1] * n
        
        # Build tree
        tree = defaultdict(list)
        for i in range(n):
            if parents[i] != -1:
                tree[parents[i]].append(i)

        # Find node with value 1
        idx = -1
        for i in range(n):
            if nums[i] == 1:
                idx = i
                break
        
        # If there's no 1 in the whole tree
        if idx == -1:
            return ans
        
        # Start from node with value 1 and go up to root
        seen = set()
        miss = 1
        curr_node = idx
        visited_nodes = set()

        while curr_node != -1:
            # Traverse only unvisited parts of the subtree
            stack = [curr_node]
            while stack:
                node = stack.pop()
                if node in visited_nodes:
                    continue
                visited_nodes.add(node)
                val = nums[node]
                seen.add(val)
                for child in tree[node]:
                    stack.append(child)
            
            # Update missing value
            while miss in seen:
                miss += 1
            ans[curr_node] = miss
            
            # Move to parent
            curr_node = parents[curr_node]
        
        return ans