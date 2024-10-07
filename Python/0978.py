class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        # Initialize variables to keep track of the max turbulent subarray length
        max_len = 1  # Minimum turbulent subarray length is 1
        up = 1  # Length of the subarray where arr[i] > arr[i+1] alternates with arr[i] < arr[i+1]
        down = 1  # Length of the subarray where arr[i] < arr[i+1] alternates with arr[i] > arr[i+1]

        # Iterate through the array
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1  # Continue the 'up' trend, hence lengthening the sequence
                down = 1  # Reset down because we are in the "up" mode
            elif arr[i] < arr[i - 1]:
                down = up + 1  # Continue the 'down' trend, hence lengthening the sequence
                up = 1  # Reset up because we are in the "down" mode
            else:
                # If arr[i] == arr[i-1], reset both counters
                up = down = 1
            
            # Track the maximum length found so far
            max_len = max(max_len, up, down)
        
        return max_len
