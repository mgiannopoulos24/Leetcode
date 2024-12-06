class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize result list
        result = []
        
        # Iterate over both strings in a zipped manner
        for char1, char2 in zip(word1, word2):
            result.append(char1)
            result.append(char2)
        
        # Append the remaining characters from word1, if any
        result.extend(word1[len(word2):])
        
        # Append the remaining characters from word2, if any
        result.extend(word2[len(word1):])
        
        # Join the result list into a single string and return it
        return ''.join(result)
