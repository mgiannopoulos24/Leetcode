# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string using pre-order traversal."""
        def preorder(node):
            if node is None:
                return ['#']  # Use '#' as a marker for None
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        
        return ','.join(preorder(root))
    
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree using pre-order traversal."""
        def build_tree(values):
            val = next(values)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build_tree(values)
            node.right = build_tree(values)
            return node
        
        values = iter(data.split(','))
        return build_tree(values)
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans