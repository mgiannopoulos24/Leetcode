class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # Function to convert a word to its numerical value
        def word_to_number(word: str) -> int:
            return int(''.join(str(ord(char) - ord('a')) for char in word))

        # Compute the numerical values
        num1 = word_to_number(firstWord)
        num2 = word_to_number(secondWord)
        target = word_to_number(targetWord)

        # Check if the sum equals the target
        return num1 + num2 == target
