class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Dictionary to store the first occurrence of each character
        first_occurrence = {}
        max_length = -1
        
        # Iterate through the string
        for i, char in enumerate(s):
            if char in first_occurrence:
                # Calculate the length of the substring between first and current occurrence
                length = i - first_occurrence[char] - 1
                max_length = max(max_length, length)
            else:
                # Store the first occurrence of the character
                first_occurrence[char] = i
        
        return max_length
