class Solution:
    def evaluate(self, expression: str) -> int:
        # A list of dictionaries to simulate scope, with each dictionary being a scope level
        scope = [{}]
        
        def evaluate_expr(expr: str) -> int:
            # If the expression is a number (or negative number), return the integer value
            if expr[0].isdigit() or expr[0] == '-':
                return int(expr)
            
            # If the expression is a variable, find it in the current scope
            if expr[0].isalpha():
                for s in reversed(scope):
                    if expr in s:
                        return s[expr]
            
            # This is a complex expression, process it recursively
            tokens = parse_tokens(expr[1:-1])  # Strip outer parentheses and parse tokens
            if tokens[0] == "let":
                # Create a new scope
                new_scope = scope[-1].copy()  # Copy the current scope
                scope.append(new_scope)
                
                # Process assignments in the let expression
                for i in range(1, len(tokens) - 1, 2):
                    var = tokens[i]
                    if i + 1 < len(tokens):
                        value = evaluate_expr(tokens[i + 1])
                        scope[-1][var] = value
                
                # The result is the evaluation of the last expression
                result = evaluate_expr(tokens[-1])
                
                # Pop the current scope after evaluation
                scope.pop()
                return result
            
            elif tokens[0] == "add":
                return evaluate_expr(tokens[1]) + evaluate_expr(tokens[2])
            
            elif tokens[0] == "mult":
                return evaluate_expr(tokens[1]) * evaluate_expr(tokens[2])
        
        def parse_tokens(expr: str) -> list:
            """ Parses tokens from an expression by balancing parentheses """
            tokens = []
            bal = 0  # Balance of parentheses
            token_start = 0
            for i, c in enumerate(expr):
                if c == '(':
                    bal += 1
                elif c == ')':
                    bal -= 1
                elif c == ' ' and bal == 0:
                    tokens.append(expr[token_start:i])
                    token_start = i + 1
            
            tokens.append(expr[token_start:])  # Add the last token
            return tokens

        # Start the evaluation
        return evaluate_expr(expression)
