class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Count how many chips are at even positions and how many are at odd positions
        even_count = 0
        odd_count = 0
        
        for pos in position:
            if pos % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        # The minimum cost is the smaller of the two counts
        return min(even_count, odd_count)
