import heapq

class StockPrice:

    def __init__(self):
        self.timestamp_to_price = {}
        self.max_heap = []
        self.min_heap = []
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_to_price[timestamp] = price
        if timestamp > self.latest_timestamp:
            self.latest_timestamp = timestamp
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.timestamp_to_price[self.latest_timestamp]

    def maximum(self) -> int:
        while self.max_heap:
            price, timestamp = self.max_heap[0]
            if self.timestamp_to_price[timestamp] == -price:
                return -price
            heapq.heappop(self.max_heap)
        return -1  # Should not reach here if update is called at least once

    def minimum(self) -> int:
        while self.min_heap:
            price, timestamp = self.min_heap[0]
            if self.timestamp_to_price[timestamp] == price:
                return price
            heapq.heappop(self.min_heap)
        return -1  # Should not reach here if update is called at least once