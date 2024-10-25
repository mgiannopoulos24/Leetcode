class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # Step 1: Generate all cells in the matrix
        all_cells = [(r, c) for r in range(rows) for c in range(cols)]
        
        # Step 2: Sort the cells by their distance to (rCenter, cCenter)
        all_cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        
        # Step 3: Return the sorted list of cells
        return all_cells
