from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        # Helper function to convert a number i to (r, c) coordinates on the board
        def num_to_position(num):
            # num is 1-based, so we subtract 1 to work in 0-based indexing
            num -= 1
            r = n - 1 - num // n  # row number from the bottom
            c = num % n
            # If the row is an odd row (0-indexed), reverse the column direction
            if (n - 1 - r) % 2 == 1:
                c = n - 1 - c
            return r, c

        # BFS setup
        queue = deque([(1, 0)])  # Start from square 1, with 0 moves
        visited = set([1])  # Track visited squares

        while queue:
            curr, moves = queue.popleft()

            # If we reached the last square, return the number of moves
            if curr == n * n:
                return moves

            # Try moving to next positions by rolling the die (1 to 6)
            for i in range(1, 7):
                next_square = curr + i
                if next_square > n * n:
                    break  # Don't go beyond the last square

                # Get the corresponding position on the board
                r, c = num_to_position(next_square)

                # If there's a snake or ladder, move to that destination
                if board[r][c] != -1:
                    next_square = board[r][c]

                # If this square hasn't been visited yet, add it to the queue
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        # If we exhaust the BFS without reaching the last square, return -1
        return -1
