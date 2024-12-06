from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n  # Initialize the result array with zeros

        if k == 0:
            return result  # Return [0, 0, 0, ..., 0] if k is 0

        # Calculate the sum for each position
        for i in range(n):
            if k > 0:
                # Sum the next k elements
                for j in range(1, k + 1):
                    result[i] += code[(i + j) % n]
            elif k < 0:
                # Sum the previous k elements
                for j in range(1, -k + 1):
                    result[i] += code[(i - j + n) % n]  # n is added to ensure non-negative index

        return result
