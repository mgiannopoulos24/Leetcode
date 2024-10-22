# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # Step 1: Convert the linked list to an array
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        n = len(values)
        result = [0] * n  # Initialize the result array with 0s
        stack = []  # This will store indices of nodes

        # Step 2: Traverse the array and use a stack to find the next greater element
        for i in range(n):
            # While the stack is not empty and the current value is greater than the value
            # at the index stored at the top of the stack, pop the stack and update result
            while stack and values[i] > values[stack[-1]]:
                index = stack.pop()
                result[index] = values[i]
            
            # Push the current index onto the stack
            stack.append(i)
        
        return result
