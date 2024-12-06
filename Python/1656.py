class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n  # Initialize the stream with None
        self.ptr = 0  # Pointer to track the next expected idKey

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value  # Place the value in the correct position
        result = []
        
        # While we have the expected value at the current pointer
        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])  # Add it to the result
            self.ptr += 1  # Move the pointer forward
        
        return result



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)