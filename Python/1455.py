class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()  # Split sentence into words
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1  # Return 1-based index
        return -1  # If no prefix match found
