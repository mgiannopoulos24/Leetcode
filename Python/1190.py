class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current_string = []
        
        for char in s:
            if char == '(':
                # Push the current string to the stack and reset it
                stack.append(current_string)
                current_string = []
            elif char == ')':
                # Reverse the current string and append it to the last string on the stack
                current_string.reverse()
                previous_string = stack.pop()
                current_string = previous_string + current_string
            else:
                # Append characters to the current string
                current_string.append(char)
        
        # Return the joined result
        return ''.join(current_string)
