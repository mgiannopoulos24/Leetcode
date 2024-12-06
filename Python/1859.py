class Solution:
    def sortSentence(self, s: str) -> str:
        # Split the sentence into words
        words = s.split()
        
        # Sort words based on the numeric suffix
        sorted_words = sorted(words, key=lambda word: int(word[-1]))
        
        # Remove the numeric suffix and join the sorted words
        original_sentence = " ".join(word[:-1] for word in sorted_words)
        
        return original_sentence
