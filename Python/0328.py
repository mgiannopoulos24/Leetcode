from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even
        
        # Rearrange the nodes
        while even and even.next:
            odd.next = even.next  # Link the next odd node
            odd = odd.next  # Move the odd pointer forward
            even.next = odd.next  # Link the next even node
            even = even.next  # Move the even pointer forward
        
        odd.next = even_head  # Connect the end of odd list to the head of even list
        
        return head