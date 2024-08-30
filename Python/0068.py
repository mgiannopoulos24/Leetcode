from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        current_words = []
        current_length = 0
        
        # Helper function to create a justified line
        def create_line(words, maxWidth, is_last_line):
            total_length = sum(len(word) for word in words)
            total_spaces = maxWidth - total_length
            if len(words) == 1 or is_last_line:
                # Last line or a single word line
                return ' '.join(words) + ' ' * (maxWidth - total_length - len(words) + 1)
            
            # Calculate the number of spaces between words
            gaps = len(words) - 1
            spaces = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            
            line = ''
            for i in range(gaps):
                line += words[i]
                line += ' ' * (spaces + (1 if i < extra_spaces else 0))
            line += words[-1]
            return line
        
        for word in words:
            if current_length + len(word) + len(current_words) > maxWidth:
                res.append(create_line(current_words, maxWidth, is_last_line=False))
                current_words = []
                current_length = 0
            current_words.append(word)
            current_length += len(word)
        
        # Add the last line
        if current_words:
            res.append(create_line(current_words, maxWidth, is_last_line=True))
        
        return res
