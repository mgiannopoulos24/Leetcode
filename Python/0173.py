from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the top node, which is the smallest node
        node = self.stack.pop()
        # If the node has a right child, push all nodes from the right child's left subtree
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        # If the stack is not empty, there are more nodes to process
        return len(self.stack) > 0
