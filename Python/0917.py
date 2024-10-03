class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Step 1: Collect all letters from the string
        letters = [char for char in s if char.isalpha()]
        
        # Step 2: Reverse the collected letters
        letters.reverse()
        
        # Step 3: Rebuild the string with reversed letters
        result = []
        for char in s:
            if char.isalpha():
                result.append(letters.pop(0))  # Replace with next letter from reversed list
            else:
                result.append(char)  # Keep non-letters in place
        
        return ''.join(result)
