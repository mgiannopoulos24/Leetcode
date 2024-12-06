class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for char in s:
            # Check if the stack is not empty and the current char forms a bad pair with the top of the stack
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop()  # Remove the bad pair
            else:
                stack.append(char)  # Add the current char to the stack
        
        # Join the stack to form the resulting string
        return ''.join(stack)
