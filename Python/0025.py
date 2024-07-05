class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a linked list segment
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            prev, curr = None, start
            while curr != end:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev

        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Find the k+1-th node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next
            # Reverse the group
            prev, curr = group_prev.next, group_prev.next.next
            for _ in range(k - 1):
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            
            start = group_prev.next
            start.next = group_next
            group_prev.next = prev
            group_prev = start