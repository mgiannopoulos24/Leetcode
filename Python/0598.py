from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Initialize min_ai and min_bi with the matrix dimensions
        min_ai = m
        min_bi = n
        
        # Iterate through the operations to find the minimum ai and bi
        for op in ops:
            ai, bi = op
            min_ai = min(min_ai, ai)
            min_bi = min(min_bi, bi)
        
        # The result is the area of the smallest rectangle defined by min_ai and min_bi
        return min_ai * min_bi
