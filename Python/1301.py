from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # Initialize DP arrays
        dp_sum = [[-float('inf')] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
        # Start position 'E' at (0,0)
        dp_sum[0][0] = 0
        dp_count[0][0] = 1
        
        for i in range(n):
            for j in range(n):
                # Skip the starting cell 'E'
                if i == 0 and j == 0:
                    continue
                # If current cell is an obstacle, skip
                if board[i][j] == 'X':
                    continue
                # Possible directions: from up, left, up-left
                from_cells = []
                if i > 0 and board[i-1][j] != 'X':
                    from_cells.append((i-1, j))
                if j > 0 and board[i][j-1] != 'X':
                    from_cells.append((i, j-1))
                if i > 0 and j > 0 and board[i-1][j-1] != 'X':
                    from_cells.append((i-1, j-1))
                
                for pi, pj in from_cells:
                    if dp_sum[pi][pj] == -float('inf'):
                        continue
                    # Current cell's value
                    if board[i][j].isdigit():
                        current_val = int(board[i][j])
                    else:
                        # 'E' or 'S'
                        current_val = 0
                    new_sum = dp_sum[pi][pj] + current_val
                    if new_sum > dp_sum[i][j]:
                        dp_sum[i][j] = new_sum
                        dp_count[i][j] = dp_count[pi][pj]
                    elif new_sum == dp_sum[i][j]:
                        dp_count[i][j] = (dp_count[i][j] + dp_count[pi][pj]) % MOD
        # End position 'S' at (n-1, n-1)
        end_sum = dp_sum[n-1][n-1]
        end_count = dp_count[n-1][n-1]
        
        if end_sum == -float('inf'):
            return [0,0]
        else:
            return [end_sum, end_count]
