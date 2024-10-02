class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding  # Store the encoded array
        self.index = 0            # Start from the first pair in the encoding

    def next(self, n: int) -> int:
        # While there are elements left in the encoding array
        while self.index < len(self.encoding):
            # Current count of the value
            count = self.encoding[self.index]
            value = self.encoding[self.index + 1]

            if n <= count:
                # If n can be fully consumed within this run
                self.encoding[self.index] -= n  # Reduce the count
                return value  # Return the current value
            else:
                # If we exhaust all elements of this run
                n -= count
                self.index += 2  # Move to the next run

        # If we run out of elements, return -1
        return -1

# Example usage:
# rLEIterator = RLEIterator([3, 8, 0, 9, 2, 5])
# print(rLEIterator.next(2))  # Returns 8
# print(rLEIterator.next(1))  # Returns 8
# print(rLEIterator.next(1))  # Returns 5
# print(rLEIterator.next(2))  # Returns -1
