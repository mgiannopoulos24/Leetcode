# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(tree_node: TreeNode, list_node: ListNode) -> bool:
            if not list_node:
                return True
            if not tree_node:
                return False
            if tree_node.val != list_node.val:
                return False
            # Continue the search down the tree
            return (dfs(tree_node.left, list_node.next) or 
                    dfs(tree_node.right, list_node.next))
        
        def search_tree(node: TreeNode, head: ListNode) -> bool:
            if not node:
                return False
            # Check if current node starts a path that matches the linked list
            if dfs(node, head):
                return True
            # Continue search in the left and right subtrees
            return (search_tree(node.left, head) or 
                    search_tree(node.right, head))
        
        # Start the search from the root of the tree
        return search_tree(root, head)