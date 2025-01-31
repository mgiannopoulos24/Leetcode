import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        # Split the sentence into tokens based on spaces
        tokens = sentence.split()
        
        valid_count = 0
        
        for token in tokens:
            # Check if the token contains any digits
            if any(char.isdigit() for char in token):
                continue
            
            # Check for hyphen validity
            hyphen_count = token.count('-')
            if hyphen_count > 1:
                continue
            elif hyphen_count == 1:
                hyphen_index = token.find('-')
                if hyphen_index == 0 or hyphen_index == len(token) - 1:
                    continue
                if not (token[hyphen_index - 1].islower() and token[hyphen_index + 1].islower()):
                    continue
            
            # Check for punctuation validity
            punctuation_count = sum(1 for char in token if char in {'!', '.', ','})
            if punctuation_count > 1:
                continue
            elif punctuation_count == 1:
                punctuation_char = next((char for char in token if char in {'!', '.', ','}), None)
                if token[-1] != punctuation_char:
                    continue
            
            # If all checks pass, increment the valid count
            valid_count += 1
        
        return valid_count