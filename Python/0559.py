# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0
            if not node.children:
                return 1
            return 1 + max(dfs(child) for child in node.children)

        return dfs(root)
