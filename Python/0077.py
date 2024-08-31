from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            # If the combination is done
            if len(path) == k:
                results.append(path[:])
                return
            
            # Go through all numbers from `start` to `n`
            for i in range(start, n + 1):
                path.append(i)             # Add number to the current combination
                backtrack(i + 1, path)    # Recurse with the next start number
                path.pop()                # Remove the last added number to backtrack

        results = []
        backtrack(1, [])
        return results