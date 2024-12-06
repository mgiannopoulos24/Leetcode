class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # Step 1: Find the minimum in each row
        min_in_rows = [(min(row), row.index(min(row))) for row in matrix]
        
        # Step 2: Find the maximum in each column
        max_in_cols = [max(col) for col in zip(*matrix)]
        
        # Step 3: Collect all lucky numbers (min in row and max in column)
        lucky_numbers = []
        for value, col in min_in_rows:
            if value == max_in_cols[col]:
                lucky_numbers.append(value)
        
        return lucky_numbers
