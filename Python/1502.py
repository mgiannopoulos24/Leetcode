class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Calculate the common difference
        diff = arr[1] - arr[0]
        
        # Step 3: Check if all consecutive pairs have the same difference
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        
        return True
