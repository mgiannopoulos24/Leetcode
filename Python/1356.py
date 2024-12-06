class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Sort the array by two keys:
        # 1. The number of 1's in the binary representation
        # 2. The number itself (for tie-breaking)
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))
