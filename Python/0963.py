from itertools import combinations
from collections import defaultdict
import math

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        point_set = set(map(tuple, points))  # Convert to a set for fast lookup
        min_area = float('inf')  # Start with an infinitely large area
        found_rectangle = False  # Track if we find any valid rectangle
        
        # Dictionary to store midpoint and diagonal squared distance
        mid_diag_map = defaultdict(list)
        
        # Check all pairs of points
        for p1, p2 in combinations(points, 2):
            # Midpoint of the diagonal
            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2
            # Squared length of the diagonal
            diag_len_sq = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            
            # Store pairs with the same midpoint and diagonal length
            mid_diag_map[(mid_x, mid_y, diag_len_sq)].append((p1, p2))
        
        # Now look for rectangles in the stored midpoints and diagonals
        for pairs in mid_diag_map.values():
            if len(pairs) < 2:
                continue  # Need at least two pairs to form a rectangle
            
            # For each pair of diagonals that share the same midpoint and diagonal length
            for (p1, p2), (p3, p4) in combinations(pairs, 2):
                # Calculate the area of the rectangle using the sides formed by p1, p3 and p1, p4
                side1_len = math.dist(p1, p3)  # Length of one side
                side2_len = math.dist(p1, p4)  # Length of adjacent side
                
                area = side1_len * side2_len
                min_area = min(min_area, area)
                found_rectangle = True  # Mark that we found a valid rectangle
        
        # If we found at least one rectangle, return the minimum area; otherwise, return 0
        return min_area if found_rectangle else 0
