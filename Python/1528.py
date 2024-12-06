class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Initialize a list of the same length as s with empty characters
        shuffled = [''] * len(s)
        
        # Place each character at the new index
        for i, char in enumerate(s):
            shuffled[indices[i]] = char
        
        # Join the list into a string and return it
        return ''.join(shuffled)
