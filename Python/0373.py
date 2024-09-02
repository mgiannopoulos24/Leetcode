from heapq import heappush, heappop
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Result list to store the k smallest pairs
        result = []
        # Min-heap (priority queue) to store pairs along with their sums
        min_heap = []
        
        # Initialize the heap with pairs from nums1[0] and all elements in nums2
        for i in range(min(len(nums1), k)):
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        # Extract k smallest pairs
        while k > 0 and min_heap:
            # Get the smallest pair from the heap
            sum_val, i, j = heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            
            # If there is a next element in nums2 for the current element of nums1
            if j + 1 < len(nums2):
                # Push the next pair into the heap
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
            
            k -= 1
        
        return result
