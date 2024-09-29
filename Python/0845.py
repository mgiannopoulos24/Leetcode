class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        
        max_length = 0
        
        # Start from the second element and go to the second-to-last element
        for i in range(1, n - 1):
            # Find a peak (i.e., arr[i] is greater than both neighbors)
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1
                
                # Expand to the left while the elements are strictly increasing
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                
                # Expand to the right while the elements are strictly decreasing
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                # Calculate the length of the mountain and update max_length
                current_length = right - left + 1
                max_length = max(max_length, current_length)
        
        return max_length
