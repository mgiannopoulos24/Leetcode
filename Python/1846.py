class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array first
        arr.sort()
        
        # Ensure the first element is 1
        arr[0] = 1
        
        # Iterate through the array to adjust elements
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
                
        # Return the last element as it is the maximum possible value
        return arr[-1]
