class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)
        
        # Skip intervals that end before the new interval starts
        while i < n and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1
        
        # Merge intervals that overlap with the new interval
        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1
        
        new_intervals.append((left, right))
        
        # Append the remaining intervals
        while i < n:
            new_intervals.append(self.intervals[i])
            i += 1
        
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        n = len(self.intervals)
        
        while i < n and self.intervals[i][1] <= left:
            i += 1
        
        while i < n and self.intervals[i][0] < right:
            if self.intervals[i][0] <= left and self.intervals[i][1] >= right:
                return True
            i += 1
        
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)
        
        while i < n and self.intervals[i][1] <= left:
            new_intervals.append(self.intervals[i])
            i += 1
        
        while i < n and self.intervals[i][0] < right:
            if self.intervals[i][0] < left:
                new_intervals.append((self.intervals[i][0], left))
            if self.intervals[i][1] > right:
                new_intervals.append((right, self.intervals[i][1]))
            i += 1
        
        while i < n:
            new_intervals.append(self.intervals[i])
            i += 1
        
        self.intervals = new_intervals

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)