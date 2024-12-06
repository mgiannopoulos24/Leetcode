from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        length = 2 * n - 1
        result = [0] * length
        used = [False] * (n + 1)
        
        def backtrack(pos):
            if pos == length:
                return True
            
            if result[pos] != 0:
                return backtrack(pos + 1)
            
            for num in range(n, 1, -1):
                if not used[num] and pos + num < length and result[pos] == 0 and result[pos + num] == 0:
                    result[pos], result[pos + num] = num, num
                    used[num] = True
                    if backtrack(pos + 1):
                        return True
                    used[num] = False
                    result[pos], result[pos + num] = 0, 0
            
            if not used[1]:
                result[pos] = 1
                used[1] = True
                if backtrack(pos + 1):
                    return True
                used[1] = False
                result[pos] = 0
            
            return False
        
        backtrack(0)
        return result
