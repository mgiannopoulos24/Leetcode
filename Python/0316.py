class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Frequency map of all characters in the string
        freq = {char: 0 for char in s}
        for char in s:
            freq[char] += 1
        
        # Stack to store the result characters
        stack = []
        # Set to check if a character is already in the stack
        seen = set()
        
        for char in s:
            # Decrease the frequency count for the current character
            freq[char] -= 1
            
            # If the character is already in the stack, continue to the next character
            if char in seen:
                continue
            
            # While stack is not empty and the top character in the stack is greater than the current character
            # and the top character in the stack will appear later in the string (frequency > 0)
            while stack and char < stack[-1] and freq[stack[-1]] > 0:
                removed_char = stack.pop()
                seen.remove(removed_char)
            
            # Add the current character to the stack and mark it as seen
            stack.append(char)
            seen.add(char)
        
        # Convert the stack into a string to get the final result
        return ''.join(stack)
