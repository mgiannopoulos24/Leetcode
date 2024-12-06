class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Split the sentence into words
        words = s.split()
        # Take the first k words and join them with spaces
        return " ".join(words[:k])
