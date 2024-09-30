class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # Step 1: Calculate the length of the decoded string
        total_length = 0
        for char in s:
            if char.isdigit():
                total_length *= int(char)
            else:
                total_length += 1
        
        # Step 2: Reverse through the string and decode the character at the k-th position
        for i in reversed(range(len(s))):
            char = s[i]
            if char.isdigit():
                total_length //= int(char)  # Divide total length by the digit
                k %= total_length  # Reduce k within the bounds of the current string
            else:
                if k == 0 or k == total_length:  # If k corresponds to the current character
                    return char
                total_length -= 1  # Move to the previous length segment
