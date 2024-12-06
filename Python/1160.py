from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Step 1: Create a frequency map for the characters in 'chars'
        char_count = Counter(chars)
        total_length = 0
        
        # Step 2: Check each word
        for word in words:
            # Create a frequency map for the characters in the word
            word_count = Counter(word)
            
            # Step 3: Check if the word can be formed
            can_form = True
            for char in word_count:
                if word_count[char] > char_count.get(char, 0):
                    can_form = False
                    break
            
            # Step 4: If the word can be formed, add its length to the total
            if can_form:
                total_length += len(word)
        
        return total_length
