class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        n, t = len(name), len(typed)
        
        while j < t:
            if i < n and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
            j += 1
        
        return i == n
