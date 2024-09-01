# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = self.getHeight(root)
        if height == 0:
            return 1

        # Binary search to find the number of nodes in the last level
        left, right = 0, (1 << height) - 1  # (1 << height) - 1 is the maximum index at the last level
        while left <= right:
            mid = (left + right) // 2
            if self.exists(mid, height, root):
                left = mid + 1
            else:
                right = mid - 1

        # Total nodes is the sum of nodes in full levels and nodes in the last level
        return (1 << height) - 1 + right + 1

    def getHeight(self, node: TreeNode) -> int:
        height = 0
        while node.left:
            node = node.left
            height += 1
        return height

    def exists(self, index: int, height: int, node: TreeNode) -> bool:
        left, right = 0, (1 << height) - 1
        for _ in range(height):
            mid = (left + right) // 2
            if index <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None