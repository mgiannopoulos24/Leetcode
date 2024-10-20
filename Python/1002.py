from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the counter with the frequency of the first word
        common_count = Counter(words[0])
        
        # Iterate over the rest of the words
        for word in words[1:]:
            # Create a frequency counter for the current word
            word_count = Counter(word)
            # Update the common_count to keep only the minimum frequency for each character
            for char in common_count:
                common_count[char] = min(common_count[char], word_count[char])
        
        # Build the result based on the frequency in common_count
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)  # Add the character 'count' times
        
        return result
