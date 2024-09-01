class Solution:
    def reverseWords(self, s: str) -> str:
        # Strip leading and trailing spaces and split the string into words
        words = s.strip().split()
        
        # Reverse the list of words
        reversed_words = words[::-1]
        
        # Join the reversed words with a single space
        result = ' '.join(reversed_words)
        
        return result
