# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.voyage = voyage
        self.index = 0
        self.flips = []

        def dfs(node: TreeNode) -> bool:
            if not node:
                return True
            
            if node.val != self.voyage[self.index]:
                return False
            
            self.index += 1
            
            if node.left and self.index < len(self.voyage) and node.left.val != self.voyage[self.index]:
                # The left child does not match, so we need to flip
                self.flips.append(node.val)
                if not dfs(node.right) or not dfs(node.left):
                    return False
            else:
                # No flip needed, verify left and then right
                if not dfs(node.left) or not dfs(node.right):
                    return False
            
            return True
        
        return self.flips if dfs(root) else [-1]