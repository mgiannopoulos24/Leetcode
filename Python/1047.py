class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        # Traverse the string
        for char in s:
            # If the stack is not empty and the top of the stack matches the current character, pop it
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        # Return the final result by joining the characters in the stack
        return ''.join(stack)
