class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Concatenate all the strings in word1 and word2
        return ''.join(word1) == ''.join(word2)
