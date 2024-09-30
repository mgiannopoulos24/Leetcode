from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words and count occurrences
        count_s1 = Counter(s1.split())
        count_s2 = Counter(s2.split())
        
        # List to store the uncommon words
        uncommon_words = []
        
        # Check words in s1
        for word in count_s1:
            if count_s1[word] == 1 and word not in count_s2:
                uncommon_words.append(word)
        
        # Check words in s2
        for word in count_s2:
            if count_s2[word] == 1 and word not in count_s1:
                uncommon_words.append(word)
        
        return uncommon_words