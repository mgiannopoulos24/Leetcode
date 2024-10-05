class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Number of rows and columns in the input
        n = len(strs)
        m = len(strs[0])
        
        # Counter for columns that need to be deleted
        deletions = 0
        
        # Keep track of whether rows are lexicographically sorted so far
        is_sorted = [False] * (n - 1)
        
        # Check each column
        for col in range(m):
            # Assume this column does not need to be deleted
            column_is_valid = True
            
            # Check if removing this column would keep the rows sorted
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col] and not is_sorted[row - 1]:
                    # Mark that this column violates the order
                    deletions += 1
                    column_is_valid = False
                    break
            
            # If the column is valid, update sorted state
            if column_is_valid:
                for row in range(1, n):
                    if strs[row][col] > strs[row - 1][col]:
                        is_sorted[row - 1] = True
        
        return deletions
