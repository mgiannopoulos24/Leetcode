from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        # Move fast pointer n steps forward
        for _ in range(n):
            fast = fast.next
        
        # Move both fast and slow pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        return dummy.next