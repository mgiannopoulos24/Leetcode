from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Helper function to compute the cross product of vectors OA and OB
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        if len(trees) <= 1:
            return trees
        
        # Sort the points lexicographically (by x, then by y)
        trees = sorted(trees)
        
        # Build the lower hull
        lower = []
        for t in trees:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], t) < 0:
                lower.pop()
            lower.append(t)
        
        # Build the upper hull
        upper = []
        for t in reversed(trees):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], t) < 0:
                upper.pop()
            upper.append(t)
        
        # Remove the last point of each half because it's repeated at the beginning of the other half
        unique_points = set(tuple(p) for p in lower[:-1] + upper[:-1])
        
        # Convert tuples back to lists
        return [list(p) for p in unique_points]
