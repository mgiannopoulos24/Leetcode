class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # Directions: (dx, dy) for moving in 8 possible directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # vertical and horizontal
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal directions
        
        # Store the positions of queens in a set for fast lookup
        queen_positions = set(map(tuple, queens))
        
        result = []
        
        # For each direction, move step by step and check for queens
        for dx, dy in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8:  # Stay within the bounds of the board
                x += dx
                y += dy
                if (x, y) in queen_positions:
                    result.append([x, y])
                    break  # Stop searching in this direction after finding the first queen
        
        return result
