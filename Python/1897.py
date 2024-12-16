from collections import Counter
from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Count the frequency of all characters across all words
        total_count = Counter()
        for word in words:
            total_count.update(word)
        
        # Check if each character count is divisible by the number of words
        n = len(words)
        for count in total_count.values():
            if count % n != 0:
                return False
        return True
