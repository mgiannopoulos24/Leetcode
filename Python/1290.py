# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            # Shift result to the left by 1 (equivalent to multiplying by 2)
            # Then add the current node's value
            result = result * 2 + head.val
            # Move to the next node
            head = head.next
        return result
