from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert wordDict into a set for O(1) look-ups
        word_set = set(wordDict)
        memo = {}
        
        def backtrack(start: int) -> List[str]:
            # Return memoized result if exists
            if start in memo:
                return memo[start]
            
            # If we reach the end of the string, return an empty list with an empty string
            if start == len(s):
                return [""]
            
            # List to hold the results for the current start index
            sentences = []
            
            # Try every possible end index for the substring
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursively process the rest of the string
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)
            
            # Memoize the result for the current start index
            memo[start] = sentences
            return sentences
        
        # Start the backtracking from the beginning of the string
        return backtrack(0)
