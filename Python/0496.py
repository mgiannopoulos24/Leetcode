from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        # Traverse nums2 to fill the next_greater map
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Elements left in the stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Prepare the result for nums1
        result = [next_greater[num] for num in nums1]
        
        return result
