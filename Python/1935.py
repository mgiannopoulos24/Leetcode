class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Convert brokenLetters to a set for faster lookup
        broken_set = set(brokenLetters)
        # Split the text into words
        words = text.split()
        # Count words that can be typed
        count = 0
        for word in words:
            # Check if the word contains any broken letter
            if all(char not in broken_set for char in word):
                count += 1
        return count
