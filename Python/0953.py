from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping from character to its position in the alien language order
        order_map = {char: index for index, char in enumerate(order)}
        
        # Function to compare two words based on the alien language order
        def is_sorted(word1: str, word2: str) -> bool:
            # Compare characters of both words
            min_length = min(len(word1), len(word2))
            for i in range(min_length):
                if order_map[word1[i]] < order_map[word2[i]]:
                    return True
                elif order_map[word1[i]] > order_map[word2[i]]:
                    return False
            # If all compared characters are equal, check lengths
            return len(word1) <= len(word2)
        
        # Check each pair of adjacent words
        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False
        
        return True
