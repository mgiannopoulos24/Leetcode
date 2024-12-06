# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Find the k-th node from the beginning and the k-th node from the end
        kth_from_start = head
        for _ in range(k - 1):
            kth_from_start = kth_from_start.next
        
        kth_from_end = head
        for _ in range(length - k):
            kth_from_end = kth_from_end.next
        
        # Step 3: Swap the values of the two nodes
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val
        
        # Step 4: Return the modified list head
        return head