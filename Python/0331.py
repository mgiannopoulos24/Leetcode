from typing import List

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Start with one slot for the root
        slots = 1
        # Split the preorder string by commas to process each node
        nodes = preorder.split(',')
        
        for node in nodes:
            # Each node needs a slot to be placed in
            slots -= 1
            
            # If at any time, we have no slots available to place the node
            if slots < 0:
                return False
            
            # If the current node is not a null node
            if node != '#':
                # Non-null node will create two additional slots
                slots += 2
        
        # In the end, we should have exactly 0 slots remaining for a valid serialization
        return slots == 0