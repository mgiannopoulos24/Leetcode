class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        cumulative_shift = 0
        result = list(s)
        
        # Traverse the shifts array from end to start
        for i in range(n - 1, -1, -1):
            cumulative_shift += shifts[i]
            # Compute the new character after shift
            new_char = chr((ord(result[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result[i] = new_char
        
        return ''.join(result)
