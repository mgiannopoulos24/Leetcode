class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Helper function for backtracking
        def backtrack(start: int, seen: set) -> int:
            # If we have processed the entire string, return 0 (no more substrings can be made)
            if start == len(s):
                return 0
            
            max_splits = 0
            # Try all possible splits starting from current position `start`
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if substring not in seen:
                    seen.add(substring)
                    # Recursively explore the rest of the string and add 1 for the current split
                    max_splits = max(max_splits, 1 + backtrack(end, seen))
                    seen.remove(substring)  # Backtrack (remove the substring from the set)
            
            return max_splits
        
        # Start backtracking from the first character
        return backtrack(0, set())
