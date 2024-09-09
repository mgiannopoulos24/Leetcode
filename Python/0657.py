class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Count the occurrences of each move
        count_R = moves.count('R')
        count_L = moves.count('L')
        count_U = moves.count('U')
        count_D = moves.count('D')
        
        # Check if the counts balance out to return to the origin
        return count_R == count_L and count_U == count_D
