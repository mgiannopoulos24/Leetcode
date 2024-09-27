class MyCalendar:
    def __init__(self):
        self.bookings = []
        
    def book(self, start: int, end: int) -> bool:
        # Check if the new interval [start, end) overlaps with any existing intervals
        for s, e in self.bookings:
            if start < e and end > s:
                return False
        # If no overlap, add the interval to the list of bookings
        self.bookings.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)