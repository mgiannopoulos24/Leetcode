# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Dictionary to store the serialized subtree as key and list of roots as values
        subtree_map = defaultdict(list)
        # Set to track duplicate subtrees
        result = set()
        
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            # Serialize left and right subtrees
            left_serial = serialize(node.left)
            right_serial = serialize(node.right)
            # Create a unique representation of the subtree
            subtree_serial = f"{node.val},{left_serial},{right_serial}"
            # Store the serialized form and node in the map
            if subtree_serial in subtree_map:
                # If this subtree has been seen before, add the root to the result set
                if len(subtree_map[subtree_serial]) == 1:
                    result.add(node)
            subtree_map[subtree_serial].append(node)
            return subtree_serial
        
        serialize(root)
        return list(result)