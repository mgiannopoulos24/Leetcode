from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the initial prefix
        prefix = strs[0]
        
        # Iterate through the remaining strings
        for s in strs[1:]:
            # Update the prefix while there is a mismatch or until the end of the current string
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        
        return prefix
