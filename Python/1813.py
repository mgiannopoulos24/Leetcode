class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split sentences into words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # Ensure that sentence1 is always the shorter or equal length sentence
        if len(words1) > len(words2):
            words1, words2 = words2, words1

        # Try to match words from the front and back
        i, j = 0, 0
        n1, n2 = len(words1), len(words2)

        # Check words from the front
        while i < n1 and words1[i] == words2[i]:
            i += 1
        
        # Check words from the back
        while j < n1 and words1[-(j+1)] == words2[-(j+1)]:
            j += 1
        
        # Check if all words in sentence1 were matched either from the front or back
        return i + j >= n1
