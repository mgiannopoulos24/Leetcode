class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def makeLargestSpecialRecursive(s: str) -> str:
            count = 0
            start = 0
            special_substrings = []
            
            for i, char in enumerate(s):
                count += 1 if char == '1' else -1
                if count == 0:
                    # Extract the special substring
                    # Recursively apply the function on the inside part (without the outer '1' and '0')
                    special_substrings.append('1' + makeLargestSpecialRecursive(s[start + 1:i]) + '0')
                    start = i + 1
            
            # Sort substrings in reverse order to get the lexicographically largest result
            special_substrings.sort(reverse=True)
            return ''.join(special_substrings)
        
        return makeLargestSpecialRecursive(s)
