from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: If the sets of characters in both words are not the same, they cannot be transformed
        if set(word1) != set(word2):
            return False
        
        # Step 2: Count the frequency of each character in both words
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        
        # Step 3: The sorted frequencies of characters must be the same
        return sorted(freq1.values()) == sorted(freq2.values())
