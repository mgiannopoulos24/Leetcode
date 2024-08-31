# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize the queue with the root node and its depth
        queue = deque([(root, 1)])  # (node, depth)
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if it's a leaf node
            if not node.left and not node.right:
                return depth
            
            # Add left child to queue if it exists
            if node.left:
                queue.append((node.left, depth + 1))
            
            # Add right child to queue if it exists
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0  # This line should never be reached if the tree has at least one node