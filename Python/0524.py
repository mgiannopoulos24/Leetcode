from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # Helper function to check if word is a subsequence of s
        def is_subsequence(s: str, word: str) -> bool:
            it = iter(s)
            return all(char in it for char in word)
        
        # Sort dictionary by length (longest first) and then lexicographically (smallest first)
        dictionary.sort(key=lambda x: (-len(x), x))
        
        # Find the longest word which is a subsequence of s
        for word in dictionary:
            if is_subsequence(s, word):
                return word
        
        # No valid word found
        return ""
