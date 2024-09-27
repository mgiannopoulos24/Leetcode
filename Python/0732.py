class MyCalendarThree:

    def __init__(self):
        # Dictionary to hold the timeline of changes in bookings
        self.timeline = {}
        self.max_bookings = 0

    def book(self, startTime: int, endTime: int) -> int:
        # Update the timeline with the start and end times of the new booking
        if startTime in self.timeline:
            self.timeline[startTime] += 1
        else:
            self.timeline[startTime] = 1
        
        if endTime in self.timeline:
            self.timeline[endTime] -= 1
        else:
            self.timeline[endTime] = -1
        
        # Calculate the current maximum number of overlapping events
        current_active = 0
        max_active = 0
        
        # Traverse the sorted time points to calculate maximum overlap
        for time in sorted(self.timeline.keys()):
            current_active += self.timeline[time]
            if current_active > max_active:
                max_active = current_active
        
        # Update the global maximum bookings
        self.max_bookings = max(self.max_bookings, max_active)
        
        return self.max_bookings

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)