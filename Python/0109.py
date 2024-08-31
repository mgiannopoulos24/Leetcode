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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Convert linked list to array
        def convertListToArray(head: Optional[ListNode]) -> List[int]:
            array = []
            while head:
                array.append(head.val)
                head = head.next
            return array
        
        # Convert sorted array to BST
        def sortedArrayToBST(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(array[mid])
            
            root.left = sortedArrayToBST(left, mid - 1)
            root.right = sortedArrayToBST(mid + 1, right)
            
            return root
        
        # Convert the linked list to an array
        array = convertListToArray(head)
        
        # Build the BST from the array
        return sortedArrayToBST(0, len(array) - 1)