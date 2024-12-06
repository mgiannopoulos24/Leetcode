# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Use a dummy node to simplify the case where the head itself is removed
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 2: Create a hash map to store prefix sums
        prefix_sum_map = {}
        current = dummy
        prefix_sum = 0
        
        # Step 3: First pass to build the prefix sum map
        while current:
            prefix_sum += current.val
            # Store the last occurrence of each prefix sum
            prefix_sum_map[prefix_sum] = current
            current = current.next
        
        # Step 4: Second pass to actually remove zero-sum sublists
        current = dummy
        prefix_sum = 0
        while current:
            prefix_sum += current.val
            # Jump to the last occurrence of this prefix sum, skipping any nodes in between
            current.next = prefix_sum_map[prefix_sum].next
            current = current.next
        
        return dummy.next
