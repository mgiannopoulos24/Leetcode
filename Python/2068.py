class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import defaultdict

        # Count the frequency of each letter in word1 and word2
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for char in word1:
            freq1[char] += 1

        for char in word2:
            freq2[char] += 1

        # Check the difference for each letter from 'a' to 'z'
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if abs(freq1[char] - freq2[char]) > 3:
                return False

        return True