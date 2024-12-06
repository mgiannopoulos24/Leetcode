from typing import List

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Initialize an empty set to store unique characters
        unique_chars = set()
        
        # Iterate through each character in the sentence
        for char in sentence:
            unique_chars.add(char)
            # Early termination: If all 26 letters are found, return True
            if len(unique_chars) == 26:
                return True
        
        # After processing all characters, check if all letters are present
        return len(unique_chars) == 26
