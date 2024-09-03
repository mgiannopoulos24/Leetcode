class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list for easy manipulation
        s_list = list(s)
        n = len(s_list)
        
        # Process every 2k characters
        for i in range(0, n, 2 * k):
            # Reverse the first k characters of the current 2k chunk
            s_list[i:i + k] = reversed(s_list[i:i + k])
        
        # Convert the list back to a string
        return ''.join(s_list)
