from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Step 1: Compute the length of the list
        length = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # Step 2: Normalize k
        k = k % length
        if k == 0:
            return head
        
        # Step 3: Find the new tail and the new head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        old_tail.next = head
        
        return new_head
