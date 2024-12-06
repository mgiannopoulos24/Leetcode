class Solution:
    def printVertically(self, s: str) -> List[str]:
        # Split the input string into words
        words = s.split()
        
        # Get the length of the longest word
        max_len = max(len(word) for word in words)
        
        # Prepare a list to hold the vertical words
        result = []
        
        # Iterate over each column (from 0 to max_len - 1)
        for i in range(max_len):
            vertical_word = []
            # For each word, append the character at position i if it exists, else append a space
            for word in words:
                if i < len(word):
                    vertical_word.append(word[i])
                else:
                    vertical_word.append(' ')
            
            # Join the characters and strip any trailing spaces
            result.append(''.join(vertical_word).rstrip())
        
        return result
