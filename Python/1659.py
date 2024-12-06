from functools import lru_cache

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        total_cells = m * n

        # Helper functions to get and set cell types in the mask
        def get(mask, idx):
            return (mask // (3 ** idx)) % 3

        def set(mask, idx, val):
            return mask + (val - get(mask, idx)) * (3 ** idx)

        @lru_cache(None)
        def dp(pos, mask, introvertsLeft, extrovertsLeft):
            if pos == total_cells:
                return 0

            r, c = divmod(pos, n)

            if c == 0 and pos != 0:
                # Reset left neighbor at the start of a new row
                left_type = 0
            else:
                # Left neighbor type is stored in the mask at position 'n'
                left_type = get(mask, n)

            up_type = get(mask, c)

            max_happiness = 0

            # Option 1: Leave the cell empty
            next_mask = set(mask, c, 0)
            next_mask = set(next_mask, n, 0)  # Update left neighbor
            max_happiness = max(max_happiness, dp(pos + 1, next_mask, introvertsLeft, extrovertsLeft))

            # Option 2: Place an introvert
            if introvertsLeft > 0:
                happiness_gain = 120
                for neighbor_type in [left_type, up_type]:
                    if neighbor_type != 0:
                        happiness_gain -= 30
                        if neighbor_type == 1:
                            happiness_gain -= 30
                        elif neighbor_type == 2:
                            happiness_gain += 20
                next_mask = set(mask, c, 1)
                next_mask = set(next_mask, n, 1)  # Update left neighbor
                max_happiness = max(max_happiness, happiness_gain + dp(pos + 1, next_mask, introvertsLeft - 1, extrovertsLeft))

            # Option 3: Place an extrovert
            if extrovertsLeft > 0:
                happiness_gain = 40
                for neighbor_type in [left_type, up_type]:
                    if neighbor_type != 0:
                        happiness_gain += 20
                        if neighbor_type == 1:
                            happiness_gain -= 30
                        elif neighbor_type == 2:
                            happiness_gain += 20
                next_mask = set(mask, c, 2)
                next_mask = set(next_mask, n, 2)  # Update left neighbor
                max_happiness = max(max_happiness, happiness_gain + dp(pos + 1, next_mask, introvertsLeft, extrovertsLeft - 1))

            return max_happiness

        initial_mask = 0  # All cells are empty, and left neighbor is empty
        return dp(0, initial_mask, introvertsCount, extrovertsCount)
