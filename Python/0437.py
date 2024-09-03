from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            nonlocal count
            if not node:
                return
            
            # Update current path sum
            current_sum += node.val
            
            # Check if there is a prefix sum that equals current_sum - targetSum
            if current_sum - targetSum in prefix_sum_count:
                count += prefix_sum_count[current_sum - targetSum]
            
            # Update the prefix sum count
            prefix_sum_count[current_sum] += 1
            
            # Traverse the left and right children
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            
            # Revert the prefix sum count for this path
            prefix_sum_count[current_sum] -= 1
        
        count = 0
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # To handle the case when a path starts from the root
        dfs(root, 0)
        return count
