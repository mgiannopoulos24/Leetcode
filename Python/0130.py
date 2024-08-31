class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(x: int, y: int):
            # If out of bounds or at 'X' or already marked as safe, return
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            # Mark the current 'O' as safe
            board[x][y] = 'S'
            # Explore all four directions
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        # Step 1: Mark all 'O's connected to the boundary
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)
        
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m - 1][j] == 'O':
                dfs(m - 1, j)

        # Step 2: Flip surrounded 'O's to 'X's and restore 'S's to 'O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'