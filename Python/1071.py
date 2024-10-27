import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check if str1 + str2 equals str2 + str1
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Compute the GCD of the lengths of str1 and str2
        gcd_len = math.gcd(len(str1), len(str2))
        
        # Step 3: The GCD string is the prefix of str1 (or str2) of length gcd_len
        return str1[:gcd_len]
