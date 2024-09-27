class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Step 1: Create a dictionary to map pairs of blocks to possible top blocks
        patterns = {}
        for pattern in allowed:
            if (pattern[0], pattern[1]) not in patterns:
                patterns[(pattern[0], pattern[1])] = set()
            patterns[(pattern[0], pattern[1])].add(pattern[2])
        
        # Step 2: Recursive backtracking function to attempt to build the pyramid
        def can_build(current_row: str, next_row: str, index: int) -> bool:
            if len(current_row) == 1:
                return True  # We have successfully built the pyramid to the top
            
            if index == len(current_row) - 1:  # Finished building the next row
                return can_build(next_row, "", 0)  # Move to build the next row
            
            # Get the current pair of blocks to build on
            left = current_row[index]
            right = current_row[index + 1]
            
            # Check all possible blocks that can go above this pair
            if (left, right) in patterns:
                for top_block in patterns[(left, right)]:
                    # Try placing this top block and proceed to the next index
                    if can_build(current_row, next_row + top_block, index + 1):
                        return True
            
            return False  # If no configuration works, return False
        
        # Step 3: Start building the pyramid from the given bottom row
        return can_build(bottom, "", 0)
