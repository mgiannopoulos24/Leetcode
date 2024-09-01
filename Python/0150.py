from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Stack to store the operands
        stack = []

        # Iterate over each token
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                # Pop the top two elements from the stack
                right = stack.pop()
                left = stack.pop()
                
                # Perform the operation based on the token
                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                elif token == '/':
                    # Python division truncates towards negative infinity, so use int() for truncation towards zero
                    result = int(left / right)
                
                # Push the result back onto the stack
                stack.append(result)
            else:
                # Convert the token to an integer and push onto the stack
                stack.append(int(token))
        
        # The final result will be the only element in the stack
        return stack[0]
