class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # Check if both strings have the same length
        if len(start) != len(end):
            return False
        
        # Check if the number of L's, R's, and X's are the same
        if (start.count('L') != end.count('L') or
            start.count('R') != end.count('R') or
            start.count('X') != end.count('X')):
            return False
        
        # Validate the movability of L's and R's
        i, j = 0, 0
        while i < len(start) and j < len(end):
            # Skip X's in start
            while i < len(start) and start[i] == 'X':
                i += 1
            # Skip X's in end
            while j < len(end) and end[j] == 'X':
                j += 1
            # Compare L and R
            if i < len(start) and j < len(end):
                if start[i] != end[j]:
                    return False
                # L can move right but not left
                if start[i] == 'L' and i < j:
                    return False
                # R can move left but not right
                if start[i] == 'R' and i > j:
                    return False
                i += 1
                j += 1
        
        return True
