from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def squared_distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        result = 0
        for point in points:
            distance_count = defaultdict(int)
            
            for other in points:
                if point != other:
                    dist = squared_distance(point, other)
                    distance_count[dist] += 1
            
            for count in distance_count.values():
                result += count * (count - 1)
        
        return result
