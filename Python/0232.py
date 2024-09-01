class MyQueue:

    def __init__(self):
        # Initialize two stacks
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # Push element onto stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # Ensure stack2 has the elements to pop
        self._transfer()
        # Pop from stack2
        return self.stack2.pop()

    def peek(self) -> int:
        # Ensure stack2 has the elements to peek
        self._transfer()
        # Peek from stack2
        return self.stack2[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack1 and not self.stack2

    def _transfer(self) -> None:
        # Transfer elements from stack1 to stack2 if stack2 is empty
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
