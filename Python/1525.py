class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left_count = [0] * n
        right_count = [0] * n
        
        # Track distinct characters from the left side
        left_distinct = set()
        for i in range(n):
            left_distinct.add(s[i])
            left_count[i] = len(left_distinct)
        
        # Track distinct characters from the right side
        right_distinct = set()
        for i in range(n-1, -1, -1):
            right_distinct.add(s[i])
            right_count[i] = len(right_distinct)
        
        # Count good splits
        good_splits = 0
        for i in range(n-1):
            if left_count[i] == right_count[i+1]:
                good_splits += 1
        
        return good_splits
