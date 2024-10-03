from collections import Counter, defaultdict
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def max_freq_count(words):
            max_freq = defaultdict(int)
            for word in words:
                freq = Counter(word)
                for char, count in freq.items():
                    max_freq[char] = max(max_freq[char], count)
            return max_freq
        
        # 1. Compute the max frequency count needed for characters in words2
        required_freq = max_freq_count(words2)
        
        # 2. Filter words1 to find universal strings
        result = []
        for word in words1:
            word_freq = Counter(word)
            if all(word_freq[char] >= count for char, count in required_freq.items()):
                result.append(word)
        
        return result