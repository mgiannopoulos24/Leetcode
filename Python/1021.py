class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        
        for char in s:
            if char == '(':
                # Only add to result if it's not the outermost '('
                if balance > 0:
                    result.append(char)
                balance += 1
            elif char == ')':
                balance -= 1
                # Only add to result if it's not the outermost ')'
                if balance > 0:
                    result.append(char)
        
        return ''.join(result)
