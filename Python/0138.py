class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Clone nodes and interleave them with the original nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Set the random pointers for the new nodes
        current = head
        while current:
            new_node = current.next
            new_node.random = current.random.next if current.random else None
            current = new_node.next
        
        # Step 3: Separate the two lists
        old_list = head
        new_list = head.next
        new_head = new_list
        
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        
        return new_head
