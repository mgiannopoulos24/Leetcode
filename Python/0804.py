from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Morse code for each letter from 'a' to 'z'
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", 
            ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", 
            ".--", "-..-", "-.--", "--.."
        ]
        
        # This will store all unique transformations
        unique_transformations = set()
        
        # Convert each word to its Morse code transformation
        for word in words:
            transformation = ''.join(morse_code[ord(char) - ord('a')] for char in word)
            unique_transformations.add(transformation)
        
        # Return the number of unique transformations
        return len(unique_transformations)
