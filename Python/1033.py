class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        # Sort a, b, c to get them in order
        x, y, z = sorted([a, b, c])
        
        # Calculate the gaps between the stones
        gap1 = y - x - 1
        gap2 = z - y - 1
        
        # Maximum number of moves is the sum of gaps
        max_moves = gap1 + gap2
        
        # Minimum number of moves
        if gap1 == 0 and gap2 == 0:
            min_moves = 0  # Stones are already consecutive
        elif gap1 <= 1 or gap2 <= 1:
            min_moves = 1  # If there's at least one adjacent pair, only 1 move is needed
        else:
            min_moves = 2  # Otherwise, it will take at least 2 moves
        
        return [min_moves, max_moves]
