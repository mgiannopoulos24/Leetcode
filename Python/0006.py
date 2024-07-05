class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If numRows is 1, return the string itself
        if numRows == 1:
            return s
        
        # Initialize rows for zigzag pattern
        rows = [''] * numRows
        index = 0
        down = False
        
        # Traverse through each character in the string
        for char in s:
            rows[index] += char
            if index == 0 or index == numRows - 1:
                down = not down
            index += 1 if down else -1
        
        # Concatenate all rows to form the result
        return ''.join(rows)
