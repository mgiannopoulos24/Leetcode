class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # Loop through the array, but stop at len(arr) - 2 to avoid out of bounds
        for i in range(len(arr) - 2):
            # Check if arr[i], arr[i+1], and arr[i+2] are all odd
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                return True
        return False
