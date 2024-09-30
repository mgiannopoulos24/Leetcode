class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  # Initialize stack with a base score of 0
        for char in s:
            if char == '(':
                stack.append(0)  # Start a new level
            else:
                top = stack.pop()  # Score of the current level
                if top == 0:
                    # Case "()": score 1
                    stack[-1] += 1
                else:
                    # Case "(A)": score 2 * score of A
                    stack[-1] += 2 * top
        return stack[0]  # The final score is at the top of the stack
