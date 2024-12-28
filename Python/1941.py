class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Create a dictionary to count occurrences of each character
        char_count = {}
        
        # Count the occurrences of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Get the set of frequencies of characters
        frequencies = set(char_count.values())
        
        # If all characters have the same frequency, the set will have one unique element
        return len(frequencies) == 1
