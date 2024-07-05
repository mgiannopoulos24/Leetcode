# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2:
            # Get the current values from the lists, or 0 if the list has been fully traversed
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum of the current digits plus any carry from the previous digit
            total = carry + x + y
            carry = total // 10  # Update carry for the next iteration
            current.next = ListNode(total % 10)  # Create a new node with the digit value
            current = current.next  # Move to the next node in the result list

            # Move to the next nodes in the input lists, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # If there is a remaining carry, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next  # Return the next node of the dummy, which is the head of the result list