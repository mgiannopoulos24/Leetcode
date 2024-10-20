class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            # Push the character onto the stack
            stack.append(char)
            
            # Check if the top three characters form "abc"
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                # Pop them from the stack
                stack.pop()
                stack.pop()
                stack.pop()
        
        # If the stack is empty, the string is valid
        return not stack
