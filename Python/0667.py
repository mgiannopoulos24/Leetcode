from typing import List

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # Start with the base pattern of length k + 1
        result = []
        for i in range(1, k + 2):
            if i % 2 == 1:  # Odd index, add from start to end
                result.append((i + 1) // 2)
            else:  # Even index, add from end to start
                result.append(k + 2 - (i // 2))
        
        # Add the remaining numbers in increasing order
        for i in range(k + 2, n + 1):
            result.append(i)
        
        return result