from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the list
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            # Reverse the first half while finding the middle
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Step 2: Handle odd-sized lists
        second_half = slow
        if fast:  # odd number of elements
            second_half = slow.next

        # Step 3: Compare the two halves
        first_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
