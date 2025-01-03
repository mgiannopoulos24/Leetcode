from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = deque()
        queue.append((root, 0))  # (node, position)
        
        while queue:
            level_size = len(queue)
            _, first_pos = queue[0]
            _, last_pos = queue[-1]
            max_width = max(max_width, last_pos - first_pos + 1)
            
            for _ in range(level_size):
                node, pos = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
        
        return max_width