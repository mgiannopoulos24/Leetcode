class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        # Initialize an array to store the minimum length of subarrays with sum = target until each index
        min_len = [float('inf')] * n
        
        # Initialize variables
        current_sum = 0
        left = 0
        min_total_length = float('inf')
        best_so_far = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window if current_sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
            
            # If we find a subarray with sum = target
            if current_sum == target:
                current_length = right - left + 1
                
                # If we have seen a valid subarray before this one, update the answer
                if left > 0 and min_len[left - 1] != float('inf'):
                    min_total_length = min(min_total_length, current_length + min_len[left - 1])
                
                # Update the minimum length of subarrays with sum = target so far
                best_so_far = min(best_so_far, current_length)
            
            # Store the best so far for the next elements
            min_len[right] = best_so_far
        
        return min_total_length if min_total_length != float('inf') else -1
