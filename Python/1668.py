class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        # Keep checking if word * (k + 1) is a substring of the sequence
        while word * (k + 1) in sequence:
            k += 1
        return k
