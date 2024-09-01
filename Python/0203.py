from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Create a dummy node that points to the head
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize the current node to the dummy node
        current = dummy
        
        # Traverse through the linked list
        while current.next:
            if current.next.val == val:
                # Skip the node with the value equal to val
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the new head, which is the next node of dummy
        return dummy.next
