# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            # Create a new root with the given value
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        # Initialize a queue for BFS
        queue = deque([root])
        current_depth = 1
        
        # Traverse the tree to the level just before the target depth
        while queue and current_depth < depth - 1:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            current_depth += 1

        # Add the new row of nodes at the target depth
        while queue:
            node = queue.popleft()
            # Create new nodes with value `val`
            old_left = node.left
            old_right = node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = old_left
            node.right.right = old_right
        
        return root
        