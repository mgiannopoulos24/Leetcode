class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n  # Initialize the LPS array
        
        # Build the LPS array
        length = 0  # Length of the previous longest prefix suffix
        i = 1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # Try a shorter prefix
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        # The last value of the LPS array will give us the length of the longest happy prefix
        longest_happy_prefix_length = lps[-1]
        
        # Return the substring from 0 to the length of the longest happy prefix
        return s[:longest_happy_prefix_length] if longest_happy_prefix_length > 0 else ""
