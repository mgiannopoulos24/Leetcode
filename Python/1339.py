# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Calculate the total sum of the tree
        def calculate_total_sum(node):
            if not node:
                return 0
            return node.val + calculate_total_sum(node.left) + calculate_total_sum(node.right)
        
        total_sum = calculate_total_sum(root)
        
        # Step 2: Calculate the maximum product by trying to split at every possible subtree
        max_product = 0
        
        def calculate_subtree_sum(node):
            nonlocal max_product
            if not node:
                return 0
            
            # Calculate the sum of the current subtree
            subtree_sum = node.val + calculate_subtree_sum(node.left) + calculate_subtree_sum(node.right)
            
            # Calculate the product of splitting at this subtree
            product = subtree_sum * (total_sum - subtree_sum)
            max_product = max(max_product, product)
            
            return subtree_sum
        
        calculate_subtree_sum(root)
        
        # Step 3: Return the maximum product modulo 10^9 + 7
        return max_product % MOD
