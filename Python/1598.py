class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0  # This will keep track of the current folder depth
        
        for log in logs:
            if log == "../":
                if depth > 0:
                    depth -= 1  # Go back to the parent folder if we're not already at the root
            elif log == "./":
                continue  # Stay in the same folder, do nothing
            else:
                depth += 1  # Move into a new folder
        
        return depth  # The depth represents how many levels deep we are
