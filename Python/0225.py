from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        # Add the new element to queue1
        self.queue1.append(x)
        
        # Move all elements from queue2 to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())
        
        # Swap the roles of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        # Remove the element from queue2 (top of the stack)
        return self.queue2.popleft()

    def top(self) -> int:
        # Peek the element from queue2 (top of the stack)
        return self.queue2[0]

    def empty(self) -> bool:
        # Check if queue2 is empty
        return not self.queue2


