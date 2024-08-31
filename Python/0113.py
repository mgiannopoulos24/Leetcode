# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node: Optional[TreeNode], currentPath: List[int], currentSum: int):
            if not node:
                return
            
            # Include the current node in the path
            currentPath.append(node.val)
            currentSum += node.val
            
            # Check if the current node is a leaf and if the path sum equals the targetSum
            if not node.left and not node.right:
                if currentSum == targetSum:
                    result.append(list(currentPath))
            else:
                # Continue to explore the left and right subtree
                dfs(node.left, currentPath, currentSum)
                dfs(node.right, currentPath, currentSum)
            
            # Backtrack: Remove the current node from the path
            currentPath.pop()
        
        result = []
        dfs(root, [], 0)
        return result