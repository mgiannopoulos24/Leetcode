from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap to store (node value, index in lists, node)
        min_heap = []
        
        # Initialize the heap with the first node of each list
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        
        # Dummy head to help with the merge process
        dummy = ListNode()
        current = dummy
        
        while min_heap:
            # Get the smallest node from the heap
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # If there is a next node, add it to the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next