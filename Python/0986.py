from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        
        while i < len(firstList) and j < len(secondList):
            # Find the intersection between firstList[i] and secondList[j]
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]
            
            # The start and end of the intersection interval
            start = max(start1, start2)
            end = min(end1, end2)
            
            # If start is less than or equal to end, we have an intersection
            if start <= end:
                result.append([start, end])
            
            # Move the pointer that has the smaller endpoint
            if end1 < end2:
                i += 1
            else:
                j += 1
        
        return result
