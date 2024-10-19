# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        # Dictionaries to keep track of parent and depth
        parent_map = {}
        depth_map = {}
        
        # BFS queue
        queue = deque([(root, None, 0)])  # (node, parent, depth)
        
        while queue:
            node, parent, depth = queue.popleft()
            
            # Update maps
            parent_map[node.val] = parent
            depth_map[node.val] = depth
            
            # Add children to the queue
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))
        
        # Check if x and y are cousins
        if (x in depth_map and y in depth_map):
            return (depth_map[x] == depth_map[y]) and (parent_map[x] != parent_map[y])
        
        return False