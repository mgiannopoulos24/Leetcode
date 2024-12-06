class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Replace all non-digit characters with spaces
        for char in word:
            if not char.isdigit():
                word = word.replace(char, ' ')
        
        # Split by spaces to extract potential numbers
        numbers = word.split()
        
        # Convert each string to an integer to remove leading zeros and add to a set
        unique_integers = set(int(num) for num in numbers)
        
        # The result is the number of unique integers
        return len(unique_integers)
