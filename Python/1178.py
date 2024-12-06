from typing import List
from collections import defaultdict

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        For each puzzle, counts the number of words that satisfy:
        - The word contains the first letter of the puzzle.
        - Every letter in the word is in the puzzle.
        
        Args:
        words (List[str]): List of words.
        puzzles (List[str]): List of puzzles.
        
        Returns:
        List[int]: List of counts corresponding to each puzzle.
        """
        
        def word_to_bitmask(word: str) -> int:
            """
            Converts a word into a bitmask where each bit represents a unique letter in the word.
            """
            mask = 0
            for ch in word:
                mask |= 1 << (ord(ch) - ord('a'))
            return mask
        
        # Step 1: Preprocess words to count frequency of each unique bitmask
        word_count = defaultdict(int)
        for word in words:
            mask = word_to_bitmask(word)
            word_count[mask] += 1
        
        result = []
        
        # Step 2: Iterate through each puzzle and count valid words
        for puzzle in puzzles:
            # Convert puzzle to bitmask
            puzzle_mask = word_to_bitmask(puzzle)
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            
            # List to hold the positions (0 to 6) excluding the first character
            # We will generate subsets of these 6 characters
            other_chars = puzzle[1:]
            
            # Generate all possible subsets of the other 6 characters
            # There are 2^6 = 64 possible subsets
            subset_count = 1 << 6  # 64
            
            total = 0
            for subset in range(subset_count):
                # Start with the first character
                subset_mask = first_char_mask
                
                # Add characters from the subset
                for i in range(6):
                    if subset & (1 << i):
                        subset_mask |= 1 << (ord(other_chars[i]) - ord('a'))
                
                # If this subset_mask exists in word_count, add its frequency
                if subset_mask in word_count:
                    total += word_count[subset_mask]
            
            result.append(total)
        
        return result