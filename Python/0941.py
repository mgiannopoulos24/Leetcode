class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        # Array must have at least 3 elements
        if n < 3:
            return False
        
        # Find the peak of the mountain
        i = 0
        # Traverse upwards
        while i < n - 1 and arr[i] < arr[i + 1]:
            i += 1
        
        # Peak must not be the first or last element
        if i == 0 or i == n - 1:
            return False
        
        # Traverse downwards
        while i < n - 1 and arr[i] > arr[i + 1]:
            i += 1
        
        # Check if we reached the end of the array
        return i == n - 1
