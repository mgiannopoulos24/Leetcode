from typing import List

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Remove the digit from the stack if current digit is smaller than the top of the stack
            # and we still have digits left to remove
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            stack.append(digit)
        
        # If k is still greater than 0, remove the last k digits from the stack
        if k > 0:
            stack = stack[:-k]
        
        # Convert stack to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        
        # Return "0" if result is an empty string
        return result if result else "0"
