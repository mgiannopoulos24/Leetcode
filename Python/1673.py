class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            # While stack is not empty, and the current element is smaller than the top of the stack
            # and there are enough elements left in nums to still build a sequence of length k,
            # pop from the stack.
            while stack and stack[-1] > num and len(stack) + (n - i) > k:
                stack.pop()
            # Add the current element to the stack if the size of the stack is less than k.
            if len(stack) < k:
                stack.append(num)
        
        return stack
