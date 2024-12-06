class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # Base case
        if len(s) < 2:
            return ""
        
        # Check which characters are in the string
        char_set = set(s)
        
        # Find a character that breaks the "nice" condition
        for i, char in enumerate(s):
            if char.swapcase() not in char_set:
                # Split at this character and check the substrings
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                
                # Return the longest nice substring
                return left if len(left) >= len(right) else right
        
        # If no split point was found, the whole string is nice
        return s
