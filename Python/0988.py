# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Helper function for DFS traversal
        def dfs(node, path):
            nonlocal smallest
            if node is None:
                return
            
            # Add the current node's character to the path
            path.append(chr(node.val + ord('a')))
            
            # If this is a leaf node, reverse the path to form a leaf-to-root string
            if not node.left and not node.right:
                leaf_to_root = ''.join(reversed(path))
                # Compare and update the smallest string
                if smallest is None or leaf_to_root < smallest:
                    smallest = leaf_to_root
            
            # Continue DFS traversal
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
            
            # Backtrack by removing the current node's character from the path
            path.pop()
        
        # Smallest string initialized to None
        smallest = None
        # Start DFS from the root
        dfs(root, [])
        return smallest
