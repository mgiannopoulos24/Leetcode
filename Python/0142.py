from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        # Step 1: Use Floyd's Tortoise and Hare algorithm to detect a cycle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            # No cycle detected
            return None
        
        # Step 2: Find the start of the cycle
        start = head
        while start != slow:
            start = start.next
            slow = slow.next
        
        return start