class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by the ending point (ascending). 
        # If two intervals have the same end, sort by start in descending order.
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # The resulting set nums must cover every interval with at least two numbers.
        result = []
        
        for start, end in intervals:
            # Check how many elements in the result set already cover the current interval
            count = 0
            if len(result) >= 1 and result[-1] >= start:
                count += 1
            if len(result) >= 2 and result[-2] >= start:
                count += 1
            
            # If we don't have enough coverage, we need to add numbers
            if count == 0:  # No numbers cover the interval, add two numbers
                result.append(end - 1)
                result.append(end)
            elif count == 1:  # Only one number covers the interval, add one more
                result.append(end)
        
        return len(result)
