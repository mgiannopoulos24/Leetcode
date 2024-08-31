from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        # Helper function to generate all BSTs for the range [start, end]
        def generate_trees(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]
            
            all_trees = []
            for root_val in range(start, end + 1):
                # Generate all possible left subtrees
                left_subtrees = generate_trees(start, root_val - 1)
                # Generate all possible right subtrees
                right_subtrees = generate_trees(root_val + 1, end)
                
                # Combine each left and right subtree with the current root
                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            
            return all_trees
        
        # Generate trees for the range [1, n]
        return generate_trees(1, n)