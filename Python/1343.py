class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        n = len(arr)
        count = 0
        
        # Calculate the sum of the first subarray of size k
        window_sum = sum(arr[:k])
        
        # If the first subarray meets the condition, count it
        if window_sum >= target_sum:
            count += 1
        
        # Use sliding window technique to calculate the sum of subsequent subarrays
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]  # Slide the window
            if window_sum >= target_sum:
                count += 1
        
        return count
