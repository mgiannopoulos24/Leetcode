class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # Create a dummy node which will help to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy  # prev is the last node before the current segment being processed
        
        while head:
            # Check if it's a start of duplicates
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Link prev node to the next non-duplicate node
                prev.next = head.next
            else:
                # No duplicates, move prev node to current node
                prev = prev.next
            
            # Move head to the next node
            head = head.next
        
        return dummy.next