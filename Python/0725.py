# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the total length of the list
        total_length = 0
        current = head
        while current:
            total_length += 1
            current = current.next
        
        # Step 2: Determine the size of each part
        part_size = total_length // k
        extra_nodes = total_length % k
        
        # Step 3: Split the list into k parts
        parts = []
        current = head
        
        for i in range(k):
            part_head = current
            # Calculate the size of the current part
            current_part_size = part_size + (1 if extra_nodes > 0 else 0)
            if extra_nodes > 0:
                extra_nodes -= 1
            
            # Traverse the list to get the end of the current part
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            # Split the part from the list
            if current:
                next_head = current.next
                current.next = None
                current = next_head
            
            parts.append(part_head)
        
        return parts