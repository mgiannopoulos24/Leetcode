import random
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        # List of rectangles, where each rectangle is defined by [ai, bi, xi, yi]
        self.rects = rects
        self.prefix_sums = []
        self.total_area = 0
        
        # Calculate the area of each rectangle and prepare prefix sums
        for rect in rects:
            ai, bi, xi, yi = rect
            width = xi - ai + 1
            height = yi - bi + 1
            area = width * height
            self.total_area += area
            self.prefix_sums.append(self.total_area)

    def pick(self) -> List[int]:
        # Pick a random point based on the cumulative area
        target_area = random.randint(1, self.total_area)
        
        # Binary search to find the rectangle corresponding to the target area
        lo, hi = 0, len(self.prefix_sums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.prefix_sums[mid] < target_area:
                lo = mid + 1
            else:
                hi = mid
        
        rect_index = lo
        rect = self.rects[rect_index]
        ai, bi, xi, yi = rect
        
        # Compute the range within the selected rectangle
        area_before = self.prefix_sums[rect_index - 1] if rect_index > 0 else 0
        rect_area = self.prefix_sums[rect_index] - area_before
        
        # Calculate the position within the rectangle
        offset = target_area - area_before - 1
        width = xi - ai + 1
        height = yi - bi + 1
        row = offset // width
        col = offset % width
        
        return [ai + col, bi + row]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()