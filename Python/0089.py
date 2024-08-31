from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        result = [0, 1]
        
        for i in range(2, n + 1):
            # Reflect the current sequence
            reflected = [(1 << (i - 1)) | num for num in reversed(result)]
            result += reflected
        
        return result