class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def next_day(cells):
            """Compute the next state of cells based on the current state."""
            new_cells = [0] * 8
            for i in range(1, 7):  # First and last cells are always 0
                new_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            return new_cells

        seen = {}
        has_cycle = False
        cycle_length = 0

        for day in range(n):
            next_cells = tuple(next_day(cells))  # Convert to tuple for immutability and hashing

            if next_cells in seen:
                # We found a cycle
                has_cycle = True
                cycle_length = day - seen[next_cells]
                break
            else:
                # Mark this configuration with the current day
                seen[next_cells] = day
                cells = next_cells

        if has_cycle:
            # Reduce the number of days using the cycle length
            remaining_days = (n - day) % cycle_length
            for _ in range(remaining_days):
                cells = next_day(cells)

        return cells
