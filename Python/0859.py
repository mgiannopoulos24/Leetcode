class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Step 1: Check if lengths of s and goal are the same
        if len(s) != len(goal):
            return False
        
        # Step 2: If s and goal are the same, check for duplicate characters
        if s == goal:
            # Check if there is any character that occurs more than once
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False
        
        # Step 3: If s and goal are different, find the positions where they differ
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        
        # If there are exactly 2 differences, check if swapping makes them equal
        if len(diff) == 2:
            i, j = diff
            # Swap the two characters and check if it matches goal
            return s[i] == goal[j] and s[j] == goal[i]
        
        # If there are not exactly 2 differences, return False
        return False
