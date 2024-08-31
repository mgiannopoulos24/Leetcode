# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # Create two dummy heads for less and greater lists
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to the current nodes in the less and greater lists
        less = less_head
        greater = greater_head
        
        # Traverse the original list
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        
        # Ensure the end of the greater list is None
        greater.next = None
        # Connect the less list to the greater list
        less.next = greater_head.next
        
        # Return the start of the less list
        return less_head.next