# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []  # No full binary tree can be formed with an even number of nodes
        if n == 1:
            return [TreeNode(0)]  # The only full binary tree with 1 node

        all_trees = []
        for left_count in range(1, n, 2):  # Left subtree sizes: 1, 3, 5, ..., n-2
            right_count = n - 1 - left_count
            left_trees = self.allPossibleFBT(left_count)
            right_trees = self.allPossibleFBT(right_count)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)

        return all_trees