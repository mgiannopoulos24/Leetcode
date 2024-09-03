class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string into words
        words = s.split()
        
        # Step 2: Reverse each word
        reversed_words = [word[::-1] for word in words]
        
        # Step 3: Join the reversed words into a single string with spaces in between
        result = ' '.join(reversed_words)
        
        return result
