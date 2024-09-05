from typing import List
from itertools import combinations

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist2(p1, p2):
            """Compute squared distance between points p1 and p2."""
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        # Get all points
        points = [p1, p2, p3, p4]
        
        # Compute all pairwise squared distances
        distances = []
        for (i, j) in combinations(range(4), 2):
            distances.append(dist2(points[i], points[j]))
        
        # Count occurrences of each distance
        from collections import Counter
        count = Counter(distances)
        
        # We need exactly two unique distances
        if len(count) != 2:
            return False
        
        # Extract the distances and their counts
        (d1, c1), (d2, c2) = count.items()
        
        # Ensure four sides and two diagonals
        if (c1 == 4 and c2 == 2 and d2 == 2 * d1) or (c2 == 4 and c1 == 2 and d1 == 2 * d2):
            return True
        return False
