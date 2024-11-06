# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        forest = []
        
        def dfs(node, is_root):
            if not node:
                return None
            
            # Check if the current node is to be deleted
            root_deleted = node.val in to_delete_set
            
            # If it's a root and not deleted, add it to the forest
            if is_root and not root_deleted:
                forest.append(node)
            
            # Recursively process left and right children
            node.left = dfs(node.left, root_deleted)
            node.right = dfs(node.right, root_deleted)
            
            # If the node is deleted, return None to remove it
            return None if root_deleted else node
        
        # Start the DFS from the root, considering the root as a potential root of the forest
        dfs(root, True)
        
        return forest