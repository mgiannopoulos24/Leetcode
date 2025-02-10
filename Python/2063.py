class Solution:
    def countVowels(self, word: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        total = 0
        for i, char in enumerate(word):
            if char in vowels:
                total += (i + 1) * (n - i)
        return total