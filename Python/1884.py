class Solution:
    def twoEggDrop(self, n: int) -> int:
        # Using the triangular number approach to minimize drops
        drops = 0
        floors_covered = 0

        while floors_covered < n:
            drops += 1
            floors_covered += drops

        return drops
