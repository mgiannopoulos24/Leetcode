class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for char in expression:
            if char == ',':
                continue
            elif char in 'tf':
                stack.append(True if char == 't' else False)
            elif char in '!&|':
                stack.append(char)
            elif char == ')':
                values = []
                # Collect values until we find the matching operator
                while stack and type(stack[-1]) == bool:
                    values.append(stack.pop())
                
                operator = stack.pop()  # Get the operator
                
                # Evaluate the sub-expression based on the operator
                if operator == '!':
                    result = not values[0]  # NOT has only one operand
                elif operator == '&':
                    result = all(values)  # AND is true if all are true
                elif operator == '|':
                    result = any(values)  # OR is true if at least one is true
                
                stack.append(result)
        
        # The final result should be the only value left in the stack
        return stack.pop()
