from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node: Optional[TreeNode], path: str, paths: List[str]):
            if node:
                # Append the current node's value to the path
                path += str(node.val)
                # If it's a leaf node, add the path to the result
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    # Continue to traverse the left and right children
                    path += '->'  # Add the arrow for the path format
                    if node.left:
                        dfs(node.left, path, paths)
                    if node.right:
                        dfs(node.right, path, paths)
        
        result = []
        dfs(root, '', result)
        return result
