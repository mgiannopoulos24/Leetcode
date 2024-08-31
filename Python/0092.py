from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        # Create a dummy node to simplify edge cases where reversal starts at the head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        # Move `pre` to the node just before the `left` position
        for _ in range(left - 1):
            pre = pre.next
        
        # `start` is the first node of the segment to reverse
        start = pre.next
        # `then` is the node that will be moved to the front of the segment
        then = start.next
        
        # Reverse the segment from `left` to `right`
        for _ in range(right - left):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        
        return dummy.next