from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Sort words to ensure shorter or lexicographically smaller words come first
        words.sort()
        
        # Set to store buildable words
        buildable = set()
        longest_word = ""
        
        for word in words:
            # If the word can be built (i.e., its prefix is in the set of buildable words)
            if len(word) == 1 or word[:-1] in buildable:
                buildable.add(word)
                # Update longest_word if the current word is longer
                if len(word) > len(longest_word):
                    longest_word = word
        
        return longest_word