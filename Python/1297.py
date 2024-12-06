from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_count = defaultdict(int)
        max_occurrences = 0

        # Iterate through the string to get all possible substrings of size minSize
        for i in range(len(s) - minSize + 1):
            substring = s[i:i + minSize]
            if len(set(substring)) <= maxLetters:
                substring_count[substring] += 1
                max_occurrences = max(max_occurrences, substring_count[substring])

        return max_occurrences
