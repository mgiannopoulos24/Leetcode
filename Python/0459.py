class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Create the concatenated string
        ss = s + s
        # Remove the first and last characters
        ss = ss[1:-1]
        # Check if the original string is in the modified concatenated string
        return s in ss
