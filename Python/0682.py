class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Initialize the stack to keep track of the scores
        stack = []
        
        # Iterate through each operation
        for op in operations:
            if op == '+':
                # '+' operation: add the sum of the last two scores
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                # 'D' operation: double the last score
                if stack:
                    stack.append(2 * stack[-1])
            elif op == 'C':
                # 'C' operation: remove the last score
                if stack:
                    stack.pop()
            else:
                # Integer operation: add the integer to the stack
                stack.append(int(op))
        
        # Return the sum of all scores in the stack
        return sum(stack)
