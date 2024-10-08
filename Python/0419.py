from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        
        m, n = len(board), len(board[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    # Check if it's the start of a horizontal ship
                    if (j == 0 or board[i][j - 1] != 'X') and (i == 0 or board[i - 1][j] != 'X'):
                        count += 1
        
        return count
