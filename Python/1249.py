class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: Identify the positions of unmatched closing parentheses ')'
        s = list(s)  # Convert string to list to modify characters easily
        open_stack = []  # Stack to track indices of unmatched '('

        # First pass: Left to right
        for i in range(len(s)):
            if s[i] == '(':
                open_stack.append(i)  # Track opening parenthesis positions
            elif s[i] == ')':
                if open_stack:
                    open_stack.pop()  # Match closing parenthesis with an opening
                else:
                    s[i] = ''  # Remove unmatched closing parenthesis

        # Second pass: Remove unmatched opening parentheses '('
        while open_stack:
            s[open_stack.pop()] = ''  # Remove unmatched opening parenthesis

        # Rebuild the valid string
        return ''.join(s)
