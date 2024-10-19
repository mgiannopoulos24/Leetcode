# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # Dictionary to hold columns and their corresponding (row, value) pairs
        column_table = defaultdict(list)
        # Queue for BFS: contains tuples of (node, row, col)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            
            if node:
                column_table[col].append((row, node.val))
                # Add the left and right children to the queue
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
        
        # Sort the column keys and prepare the result
        result = []
        for col in sorted(column_table.keys()):
            # Sort by row first, and then by value
            column_table[col].sort(key=lambda x: (x[0], x[1]))
            # Extract sorted values
            result.append([val for row, val in column_table[col]])
        
        return result