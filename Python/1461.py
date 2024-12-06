class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # The total number of distinct binary codes of length k is 2^k
        needed_codes = 1 << k  # This is the same as 2^k
        
        # A set to keep track of all unique substrings of length k
        seen_codes = set()
        
        # Iterate over the string and extract substrings of length k
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            seen_codes.add(substring)
            
            # If we have found all needed codes, return True early
            if len(seen_codes) == needed_codes:
                return True
        
        # If after going through the string, we haven't found all codes, return False
        return len(seen_codes) == needed_codes
