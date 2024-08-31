class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, current_num: int) -> int:
            if not node:
                return 0
            # Update the current number
            current_num = current_num * 10 + node.val
            # If it's a leaf node, return the current number
            if not node.left and not node.right:
                return current_num
            # Recursively sum up numbers from the left and right subtrees
            left_sum = dfs(node.left, current_num)
            right_sum = dfs(node.right, current_num)
            return left_sum + right_sum
        
        # Start the DFS traversal from the root
        return dfs(root, 0)