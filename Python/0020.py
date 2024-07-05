class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # Initialize an empty stack to store opening brackets
        mapping = {')': '(', '}': '{', ']': '['}  # Define mapping of closing to opening brackets
        
        for char in s:
            if char in mapping.values():
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
            elif char in mapping:
                # If the character is a closing bracket
                if not stack or stack.pop() != mapping[char]:
                    # If stack is empty or top of stack does not match corresponding opening bracket
                    return False
        
        # After iterating through all characters
        return len(stack) == 0  # Return True if stack is empty, False otherwise
