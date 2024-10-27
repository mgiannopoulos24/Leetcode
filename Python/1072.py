from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = defaultdict(int)

        for row in matrix:
            # Calculate the "canonical" pattern for the row
            # We compare the row and its complement (flipped version)
            # For a row [0, 1], complement would be [1, 0]
            pattern = tuple(row)
            flipped_pattern = tuple(1 - x for x in row)
            
            # We treat both row and flipped row as the same group
            # and count the occurrence of either
            if pattern < flipped_pattern:
                patterns[pattern] += 1
            else:
                patterns[flipped_pattern] += 1

        # The result is the maximum size of any group
        return max(patterns.values())
