from math import comb
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        k = len(balls)  # number of colors
        total = sum(balls)  # total number of balls
        n = total // 2  # half of the balls

        # Precompute combinations C(color, x)
        C = [[0] * (balls[i] + 1) for i in range(k)]
        for i in range(k):
            for x in range(balls[i] + 1):
                C[i][x] = comb(balls[i], x)

        total_ways = 0
        valid_ways = 0

        def recurse(color, sum_x, distinct1, distinct2, C_prod):
            nonlocal total_ways, valid_ways
            if color == k:
                if sum_x == n:
                    total_ways += C_prod
                    if distinct1 == distinct2:
                        valid_ways += C_prod
                return
            for x in range(balls[color] + 1):
                new_sum_x = sum_x + x
                if new_sum_x > n:
                    continue
                # Update distinct counts
                new_distinct1 = distinct1 + (1 if x > 0 else 0)
                new_distinct2 = distinct2 + (1 if (balls[color] - x) > 0 else 0)
                # Update combination product
                new_C_prod = C_prod * C[color][x]
                recurse(color + 1, new_sum_x, new_distinct1, new_distinct2, new_C_prod)

        recurse(0, 0, 0, 0, 1)

        return valid_ways / total_ways