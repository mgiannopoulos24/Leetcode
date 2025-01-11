from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        # Calculate prefix sums for both rows
        top_prefix = [0] * n
        bottom_prefix = [0] * n

        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]

        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]

        # Minimum points Robot 2 can collect if both play optimally
        min_points_robot2 = float('inf')

        for i in range(n):
            # Points Robot 2 can collect after Robot 1's path
            # Points above Robot 1's transition column (top row to the right of column i)
            points_above = top_prefix[n - 1] - top_prefix[i]
            # Points below Robot 1's transition column (bottom row to the left of column i)
            points_below = bottom_prefix[i - 1] if i > 0 else 0

            # Max points Robot 2 can collect in this scenario
            max_robot2_points = max(points_above, points_below)

            # Update the minimum points Robot 2 can collect
            min_points_robot2 = min(min_points_robot2, max_robot2_points)

        return min_points_robot2
