from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Helper function to split the list into two halves
        def split(head: ListNode) -> (ListNode, ListNode):
            slow, fast = head, head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return head, slow

        # Helper function to merge two sorted lists
        def merge(left: ListNode, right: ListNode) -> ListNode:
            dummy = ListNode(0)
            current = dummy
            while left and right:
                if left.val <= right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left if left else right
            return dummy.next

        # Recursive function to sort the list
        def sort(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head
            left, right = split(head)
            left = sort(left)
            right = sort(right)
            return merge(left, right)

        return sort(head)
