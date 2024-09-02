from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dict = {word: i for i, word in enumerate(words)}
        result = []

        def is_palindrome(word):
            return word == word[::-1]

        for i, word in enumerate(words):
            word_len = len(word)
            
            for j in range(word_len + 1):
                prefix, suffix = word[:j], word[j:]
                
                # Case 1: Check if prefix is palindrome and suffix reversed exists in dictionary
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_dict and word_dict[reversed_suffix] != i:
                        result.append([word_dict[reversed_suffix], i])
                
                # Case 2: Check if suffix is palindrome and prefix reversed exists in dictionary
                # We check `j != word_len` to avoid duplicates when both prefix and suffix are palindromes
                if j != word_len and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_dict and word_dict[reversed_prefix] != i:
                        result.append([i, word_dict[reversed_prefix]])

        return result