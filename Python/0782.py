class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Helper function to count swaps needed to match a pattern
        def swap_count(lines, target):
            diff = sum(1 for i in range(n) if lines[i] != target[i])
            if n % 2 == 0:
                return min(diff, n - diff) // 2
            else:
                if diff % 2 == 1:
                    return float('inf')  # Can't fix if difference count is odd
                return diff // 2
        
        # Check if the board can be transformed into a chessboard pattern
        row_mask = board[0]
        col_mask = [board[i][0] for i in range(n)]
        
        # Validate rows and columns based on the first row and column
        for i in range(n):
            if board[i] != row_mask and board[i] != [1 - x for x in row_mask]:
                return -1
            if [board[j][i] for j in range(n)] != col_mask and [1 - board[j][i] for j in range(n)] != col_mask:
                return -1
        
        # Row and column pattern should be alternating
        row_sum = sum(row_mask)
        col_sum = sum(col_mask)
        if not (n // 2 <= row_sum <= (n + 1) // 2) or not (n // 2 <= col_sum <= (n + 1) // 2):
            return -1
        
        # Target pattern for chessboard (alternating 0s and 1s)
        row_pattern1 = [i % 2 for i in range(n)]
        row_pattern2 = [(i + 1) % 2 for i in range(n)]
        
        col_pattern1 = [i % 2 for i in range(n)]
        col_pattern2 = [(i + 1) % 2 for i in range(n)]
        
        # Calculate row and column swaps
        row_swaps = min(swap_count(row_mask, row_pattern1), swap_count(row_mask, row_pattern2))
        col_swaps = min(swap_count(col_mask, col_pattern1), swap_count(col_mask, col_pattern2))
        
        if row_swaps == float('inf') or col_swaps == float('inf'):
            return -1
        
        return row_swaps + col_swaps
