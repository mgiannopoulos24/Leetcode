class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0  # For the final result
        sign = 1    # To track the sign of the current number
        i = 0       # Index for iteration
        
        while i < len(s):
            char = s[i]
            
            if char.isdigit():
                # Build the operand
                operand = 0
                while i < len(s) and s[i].isdigit():
                    operand = operand * 10 + int(s[i])
                    i += 1
                i -= 1  # Move index back to correct position after digit parsing
                operand *= sign
                result += operand
                sign = 1  # Reset sign after adding operand
            
            elif char == '+':
                sign = 1
            
            elif char == '-':
                sign = -1
            
            elif char == '(':
                # Push current result and sign onto the stack
                stack.append(result)
                stack.append(sign)
                result = 0  # Reset result for the new sub-expression
                sign = 1
            
            elif char == ')':
                # Evaluate the sub-expression
                result *= stack.pop()  # Pop the sign
                result += stack.pop()  # Pop the stored result
            
            # Move to the next character
            i += 1
        
        return result
