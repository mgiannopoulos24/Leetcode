class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use a dummy node to handle edge cases
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev = dummy_head
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            node1 = prev.next
            node2 = prev.next.next
            
            # Perform the swap
            prev.next = node2
            node1.next = node2.next
            node2.next = node1
            
            # Move prev to the next pair
            prev = node1
        
        return dummy_head.next