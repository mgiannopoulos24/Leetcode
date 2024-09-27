from typing import List
from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: Parse the licensePlate to count the frequency of each letter
        plate_counter = Counter()
        for char in licensePlate.lower():
            if char.isalpha():
                plate_counter[char] += 1
        
        # Step 2: Define a helper function to check if a word is a completing word
        def is_completing_word(word: str) -> bool:
            word_counter = Counter(word)
            for char, count in plate_counter.items():
                if word_counter[char] < count:
                    return False
            return True
        
        # Step 3: Find the shortest completing word
        shortest_word = None
        for word in words:
            if is_completing_word(word):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word

