class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)  # Convert string to a list to modify it easily
        
        for i in range(len(s)):
            if s[i] == '?':
                # Try replacing with 'a', 'b', or 'c'
                for char in 'abc':
                    # Check if char is different from the previous and next characters
                    if (i > 0 and s[i-1] == char) or (i < len(s) - 1 and s[i+1] == char):
                        continue
                    s[i] = char
                    break
        
        return ''.join(s)
