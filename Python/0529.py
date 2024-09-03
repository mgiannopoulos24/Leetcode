from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        clickr, clickc = click
        
        def count_adjacent_mines(r: int, c: int) -> int:
            """Count the number of mines around (r, c)."""
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count
        
        def reveal(r: int, c: int):
            """Recursively reveal the cells starting from (r, c)."""
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
            
            mines_count = count_adjacent_mines(r, c)
            if mines_count > 0:
                board[r][c] = str(mines_count)
            else:
                board[r][c] = 'B'
                directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    reveal(nr, nc)
        
        if board[clickr][clickc] == 'M':
            board[clickr][clickc] = 'X'
        else:
            reveal(clickr, clickc)
        
        return board
