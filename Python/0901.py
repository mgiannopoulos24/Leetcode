class StockSpanner:

    def __init__(self):
        # Stack to store (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Start with a span of 1 for the current price
        span = 1
        
        # Calculate the span by popping from stack while the top price is <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push the current price and its span onto the stack
        self.stack.append((price, span))
        
        # Return the span for the current price
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)