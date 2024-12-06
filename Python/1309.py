class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':  # Check if the current group is a 10# to 26#
                result.append(chr(int(s[i:i+2]) + 96))  # Convert the number (10-26) to corresponding letter
                i += 3  # Skip past the current group
            else:
                result.append(chr(int(s[i]) + 96))  # Convert single digit (1-9) to corresponding letter
                i += 1  # Move to the next character
        return ''.join(result)
