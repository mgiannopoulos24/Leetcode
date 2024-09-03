class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Check if all characters are uppercase
        if word.isupper():
            return True
        # Check if all characters are lowercase
        if word.islower():
            return True
        # Check if only the first character is uppercase and the rest are lowercase
        if word[0].isupper() and word[1:].islower():
            return True
        # If none of the conditions are met, return False
        return False
