import heapq

class SeatManager:

    def __init__(self, n: int):
        # Use a min-heap to efficiently manage the smallest available seat
        self.available_seats = list(range(1, n + 1))
        heapq.heapify(self.available_seats)

    def reserve(self) -> int:
        # Pop the smallest available seat from the heap
        return heapq.heappop(self.available_seats)

    def unreserve(self, seatNumber: int) -> None:
        # Push the unreserved seat back into the heap
        heapq.heappush(self.available_seats, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)