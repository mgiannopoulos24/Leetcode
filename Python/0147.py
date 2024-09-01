from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to act as the start of the sorted list
        dummy = ListNode(float('-inf'))
        current = head
        
        while current:
            # At each step, remove the node from the current list
            prev_node = dummy
            next_node = dummy.next
            
            # Find the correct position to insert the current node
            while next_node and next_node.val < current.val:
                prev_node = next_node
                next_node = next_node.next
            
            # Insert the current node into the sorted list
            temp = current.next
            current.next = next_node
            prev_node.next = current
            current = temp
        
        return dummy.next
