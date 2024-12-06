from typing import List

class Solution:
    def arrangeWords(self, text: str) -> str:
        """
        Rearranges the words in the input text in increasing order of their lengths.
        If two words have the same length, their original order is preserved.
        The first word of the resulting sentence is capitalized, and the rest are in lowercase.
        
        Parameters:
        text (str): The original sentence.
        
        Returns:
        str: The rearranged sentence.
        """
        # Step 1: Split the sentence into words
        words = text.split()
        
        # Step 2: Sort the words by length while preserving original order for ties
        # Since Python's sorted() is stable, it preserves the original order for equal lengths
        sorted_words = sorted(words, key=lambda word: len(word))
        
        # Step 3: Convert all words to lowercase
        lowercased_words = [word.lower() for word in sorted_words]
        
        # Step 4: Capitalize the first word
        if lowercased_words:
            lowercased_words[0] = lowercased_words[0].capitalize()
        
        # Step 5: Join the words back into a single string
        rearranged_text = ' '.join(lowercased_words)
        
        return rearranged_text