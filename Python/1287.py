class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4
        
        # Check elements at 0, n/4, n/2, 3n/4 positions
        for i in [0, n // 4, n // 2, 3 * n // 4]:
            candidate = arr[i]
            # Count how many times this candidate appears
            if arr.count(candidate) > threshold:
                return candidate
        
        return -1  # We are guaranteed that one element appears more than 25%, so this won't be reached.
