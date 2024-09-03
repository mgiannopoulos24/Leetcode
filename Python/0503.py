from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n  # Initialize the result list with -1s
        stack = []  # This will store the indices of the elements
        
        # We will go through the array twice to simulate the circular array
        for i in range(2 * n):
            current_index = i % n  # Modulo operation to wrap around the circular array
            # While stack is not empty and the current element is greater than the element
            # corresponding to the index on the top of the stack
            while stack and nums[current_index] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[current_index]
            # If we are in the first pass, add index to stack
            if i < n:
                stack.append(current_index)
        
        return res
