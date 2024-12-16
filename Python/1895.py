class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Precompute prefix sums for rows and columns
        row_prefix = [[0] * (n + 1) for _ in range(m)]
        col_prefix = [[0] * (n) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
                col_prefix[i + 1][j] = col_prefix[i][j] + grid[i][j]

        def get_row_sum(row, start, end):
            return row_prefix[row][end] - row_prefix[row][start]

        def get_col_sum(col, start, end):
            return col_prefix[end][col] - col_prefix[start][col]

        # Check if a k x k subgrid starting at (x, y) is a magic square
        def is_magic(x, y, k):
            target = sum(grid[x + i][y + i] for i in range(k))
            if sum(grid[x + i][y + k - 1 - i] for i in range(k)) != target:
                return False

            for i in range(k):
                if get_row_sum(x + i, y, y + k) != target or get_col_sum(y + i, x, x + k) != target:
                    return False

            return True

        # Iterate over possible sizes of magic squares
        for size in range(min(m, n), 0, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if is_magic(i, j, size):
                        return size

        return 1
