from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, value: int) -> None:
        if value in self.intervals:
            return  # The number is already within an existing interval

        # Find the interval that might be affected
        it = self.intervals.bisect_left(value)
        
        # Initialize the new start and end of the interval
        start = value
        end = value
        
        # Check if the number extends an existing interval on the left
        if it > 0:
            prev_start = self.intervals.iloc[it - 1]
            prev_end = self.intervals[prev_start]
            if prev_end >= value - 1:
                start = prev_start
                end = max(end, prev_end)
        
        # Check if the number extends an existing interval on the right
        while it < len(self.intervals) and self.intervals.iloc[it] <= value + 1:
            end = max(end, self.intervals.pop(self.intervals.iloc[it]))
        
        # Insert the new or extended interval
        self.intervals[start] = end

    def getIntervals(self) -> list[list[int]]:
        return [[start, end] for start, end in self.intervals.items()]