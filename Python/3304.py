class Solution:
    def kthCharacter(self, k: int) -> str:
        # Start with the initial word
        word = "a"
        
        # Continue generating the word until its length exceeds or equals k
        while len(word) < k:
            # Generate the next part of the string
            next_part = ''.join(
                chr((ord(c) - ord('a') + 1) % 26 + ord('a')) for c in word
            )
            # Append the new part to the word
            word += next_part
        
        # Return the k-th character (1-indexed, so we use k-1)
        return word[k - 1]
