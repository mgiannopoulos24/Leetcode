class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head  # Start with the head of the list
        
        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate nodes
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        return head