# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            
            # Current node's balance is its value plus left and right balances minus 1
            current_balance = node.val + left_balance + right_balance - 1
            
            # Accumulate the absolute value of balance into moves
            self.moves += abs(current_balance)
            
            # Return the balance to the parent
            return current_balance
        
        dfs(root)
        return self.moves