from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Store all words in a set for O(1) lookups
        word_set = set(words)
        
        # Helper function to check if a word can be formed by concatenating other words
        def can_form(word):
            if not word:
                return False
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True  # An empty string can always be formed
            
            # Check all substrings
            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[n]
        
        # Store results
        concatenated_words = []
        
        # Check each word
        for word in words:
            # Remove the current word from the set and check if it can be formed
            word_set.remove(word)
            if can_form(word):
                concatenated_words.append(word)
            # Add the word back to the set
            word_set.add(word)
        
        return concatenated_words
