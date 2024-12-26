class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7

        # Generate all valid rows for a grid of height m
        def generate_rows(current_row, row=[]):
            if len(row) == m:
                valid_rows.append(tuple(row))
                return
            for color in range(3):  # 0=red, 1=green, 2=blue
                if not row or row[-1] != color:
                    generate_rows(current_row, row + [color])

        # Check if two rows can be adjacent
        def is_valid_transition(row1, row2):
            return all(row1[i] != row2[i] for i in range(m))

        # Step 1: Generate all valid rows
        valid_rows = []
        generate_rows([])

        # Step 2: Precompute valid transitions
        row_count = len(valid_rows)
        transitions = {i: [] for i in range(row_count)}
        for i, row1 in enumerate(valid_rows):
            for j, row2 in enumerate(valid_rows):
                if is_valid_transition(row1, row2):
                    transitions[i].append(j)

        # Step 3: Dynamic programming
        dp = [[0] * row_count for _ in range(n)]
        # Initialize first column
        for i in range(row_count):
            dp[0][i] = 1

        # Fill DP table
        for col in range(1, n):
            for i in range(row_count):
                for j in transitions[i]:
                    dp[col][i] = (dp[col][i] + dp[col - 1][j]) % MOD

        # Step 4: Sum all valid configurations for the last column
        return sum(dp[n - 1][i] for i in range(row_count)) % MOD
