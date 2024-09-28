class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # Remove duplicates by converting words into a set
        unique_words = set(words)
        
        # Eliminate all words that are suffixes of other words
        for word in words:
            for i in range(1, len(word)):
                suffix = word[i:]
                if suffix in unique_words:
                    unique_words.remove(suffix)
        
        # The result is the sum of the lengths of all remaining words plus the '#' for each word
        return sum(len(word) + 1 for word in unique_words)
