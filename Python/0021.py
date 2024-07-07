from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy node and pointers
        dummy_head = ListNode()
        current = dummy_head
        ptr1, ptr2 = list1, list2
        
        # Traverse both lists and merge
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                ptr2 = ptr2.next
            current = current.next
        
        # Append remaining nodes if any
        if ptr1:
            current.next = ptr1
        elif ptr2:
            current.next = ptr2
        
        return dummy_head.next