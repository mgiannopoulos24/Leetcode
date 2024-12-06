# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Step 1: Find the node just before 'a' (prev_a) and the node just after 'b' (post_b)
        prev_a = list1
        for i in range(a - 1):  # Move to the (a-1)th node
            prev_a = prev_a.next
        
        post_b = prev_a
        for i in range(b - a + 2):  # Move to the (b+1)th node
            post_b = post_b.next
        
        # Step 2: Connect the 'prev_a' node to the head of 'list2'
        prev_a.next = list2
        
        # Step 3: Traverse list2 to its last node
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        
        # Step 4: Connect the last node of 'list2' to 'post_b'
        tail2.next = post_b
        
        return list1
