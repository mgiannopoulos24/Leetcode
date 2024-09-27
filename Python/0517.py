class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        if total_dresses % n != 0:
            return -1
        average = total_dresses // n
        max_moves = 0
        cumulative = 0

        for dresses in machines:
            diff = dresses - average
            cumulative += diff
            max_moves = max(max_moves, abs(cumulative), diff)
        return max_moves
