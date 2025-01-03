class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s, t):
            it = iter(t)
            return all(c in it for c in s)
        
        max_length = -1
        for i, s in enumerate(strs):
            is_uncommon = True
            for j, t in enumerate(strs):
                if i != j and is_subsequence(s, t):
                    is_uncommon = False
                    break
            if is_uncommon:
                max_length = max(max_length, len(s))
        
        return max_length