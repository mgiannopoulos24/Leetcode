from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define the sets for each row of the keyboard
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        
        def canBeTypedUsingOneRow(word: str) -> bool:
            lower_word = word.lower()
            # Check which row the first character belongs to
            if lower_word[0] in row1:
                target_row = row1
            elif lower_word[0] in row2:
                target_row = row2
            else:
                target_row = row3
            
            # Verify if all characters are in the identified row
            return all(char in target_row for char in lower_word)
        
        # Filter the words based on the criteria
        return [word for word in words if canBeTypedUsingOneRow(word)]
