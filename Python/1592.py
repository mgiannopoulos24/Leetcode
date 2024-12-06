class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Step 1: Count the number of spaces in the input string
        total_spaces = text.count(' ')
        
        # Step 2: Extract the words from the input string
        words = text.split()
        num_words = len(words)
        
        # Step 3: Handle the case when there's only one word
        if num_words == 1:
            # Just append all the spaces to the single word
            return words[0] + ' ' * total_spaces
        
        # Step 4: Calculate the number of spaces to distribute between words and the remainder
        spaces_between_words = total_spaces // (num_words - 1)
        remaining_spaces = total_spaces % (num_words - 1)
        
        # Step 5: Join the words with the evenly distributed spaces between them
        result = (' ' * spaces_between_words).join(words)
        
        # Step 6: Append any remaining spaces at the end
        result += ' ' * remaining_spaces
        
        return result
