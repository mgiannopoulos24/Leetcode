from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize the row with the first element being 1
        row = [1] * (rowIndex + 1)
        
        # Compute the elements of the row
        for k in range(1, rowIndex + 1):
            # Update the value of row[k] based on the previous value
            row[k] = row[k - 1] * (rowIndex - k + 1) // k
        
        return row
