class MinStack:

    def __init__(self):
        # Initialize the main stack and the min stack
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # Push value onto the main stack
        self.stack.append(val)
        
        # If min stack is empty or the new value is less than or equal to the current minimum, push it onto the min stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop value from the main stack
        if self.stack:
            val = self.stack.pop()
            
            # If the value popped is the same as the top of the min stack, pop it from the min stack as well
            if self.min_stack and val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def getMin(self) -> int:
        # Return the top element of the min stack which is the minimum value
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")
