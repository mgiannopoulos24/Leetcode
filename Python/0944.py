class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Number of rows and columns
        num_rows = len(strs)
        num_cols = len(strs[0])
        
        # Initialize the count of columns to delete
        count_to_delete = 0
        
        # Iterate over each column
        for col in range(num_cols):
            # Check if the column is sorted
            is_sorted = True
            for row in range(1, num_rows):
                if strs[row][col] < strs[row - 1][col]:
                    is_sorted = False
                    break
            
            # If the column is not sorted, increment the count
            if not is_sorted:
                count_to_delete += 1
        
        return count_to_delete
