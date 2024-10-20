class Solution:
    def clumsy(self, n: int) -> int:
        # Initialize a stack to hold numbers and results of operations
        stack = []
        
        # First, push the first number
        stack.append(n)
        n -= 1
        
        # We will alternate between the following operations: *, /, +, -
        index = 0
        
        # While there are more numbers to process
        while n > 0:
            if index % 4 == 0:  # Multiplication
                stack.append(stack.pop() * n)
            elif index % 4 == 1:  # Division
                stack.append(int(stack.pop() / n))  # Floor division
            elif index % 4 == 2:  # Addition
                stack.append(n)
            else:  # Subtraction
                stack.append(-n)
            n -= 1
            index += 1
        
        # Sum all numbers in the stack
        return sum(stack)
