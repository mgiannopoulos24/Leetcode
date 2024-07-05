class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_index_map = {}
        # Initialize the starting index of the current window
        start = 0
        # Initialize the maximum length of substring without repeating characters
        max_length = 0

        # Iterate over the string using the index and character
        for index, char in enumerate(s):
            # If the character is already in the dictionary and is within the current window
            if char in char_index_map and char_index_map[char] >= start:
                # Move the start to the right of the last occurrence of the current character
                start = char_index_map[char] + 1

            # Update the last seen index of the current character
            char_index_map[char] = index

            # Update the maximum length found
            max_length = max(max_length, index - start + 1)

        return max_length