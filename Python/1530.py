# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        
        # Helper function for postorder traversal
        def dfs(node):
            if not node:
                return [0] * (distance + 1)
            
            # If it's a leaf node
            if not node.left and not node.right:
                dist = [0] * (distance + 1)
                dist[1] = 1  # Leaf node has distance 1 from itself
                return dist
            
            # Get distance counts from left and right subtrees
            left_dist = dfs(node.left)
            right_dist = dfs(node.right)
            
            # Count the number of good pairs between left and right leaves
            for l in range(1, distance + 1):
                for r in range(1, distance + 1):
                    if l + r <= distance:
                        self.result += left_dist[l] * right_dist[r]
            
            # Update current node's distance array
            dist = [0] * (distance + 1)
            for i in range(1, distance):
                dist[i + 1] = left_dist[i] + right_dist[i]
            
            return dist
        
        dfs(root)
        return self.result
