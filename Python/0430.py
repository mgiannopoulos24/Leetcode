# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Create a dummy node to simplify the process
        dummy = Node(0)
        prev = dummy
        stack = [head]

        while stack:
            curr = stack.pop()
            
            # Connect previous node with current node
            prev.next = curr
            curr.prev = prev
            prev = curr
            
            # If there is a next node, push it to the stack
            if curr.next:
                stack.append(curr.next)
            
            # If there is a child node, push it to the stack
            if curr.child:
                stack.append(curr.child)
                # Once we push the child, we should nullify the child pointer
                curr.child = None
        
        # The real head is the next of the dummy node
        dummy.next.prev = None
        return dummy.next
