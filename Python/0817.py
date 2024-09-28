# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        # Convert nums to a set for fast lookups
        num_set = set(nums)
        connected_components = 0
        in_component = False
        
        current = head
        while current:
            if current.val in num_set:
                if not in_component:
                    # We are starting a new component
                    connected_components += 1
                    in_component = True
            else:
                # We have exited a component
                in_component = False
            current = current.next
        
        return connected_components