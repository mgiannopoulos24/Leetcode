import bisect

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seats = []

    def seat(self) -> int:
        if not self.seats:
            self.seats.append(0)
            return 0
        
        # Calculate the gaps between consecutive seats and the ends
        max_gap = self.seats[0]  # Gap at the beginning
        seat_to_take = 0
        
        for i in range(1, len(self.seats)):
            gap = (self.seats[i] - self.seats[i-1]) // 2
            if gap > max_gap:
                max_gap = gap
                seat_to_take = self.seats[i-1] + gap
        
        # Check the gap at the end
        end_gap = self.n - 1 - self.seats[-1]
        if end_gap > max_gap:
            max_gap = end_gap
            seat_to_take = self.n - 1
        
        # Insert the new seat in the sorted list
        bisect.insort(self.seats, seat_to_take)
        return seat_to_take

    def leave(self, p: int) -> None:
        self.seats.remove(p)