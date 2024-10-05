class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0  # To track the number of missing integers
        prev = 0  # Previous number before the current one in the array
        
        # Traverse through the array
        for num in arr:
            # Count how many numbers are missing between prev and num
            missing_count += num - prev - 1
            
            # If we have found enough missing numbers
            if missing_count >= k:
                # Calculate the exact number we're missing
                return num - (missing_count - k + 1)
            
            prev = num  # Update prev to the current number
        
        # If we haven't found enough missing numbers in the array
        # The kth missing number is beyond the largest number in the array
        return arr[-1] + (k - missing_count)
