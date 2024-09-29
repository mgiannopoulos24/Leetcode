from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            # Check if mid is the peak
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                # Peak is in the right half
                left = mid + 1
            else:
                # Peak is in the left half
                right = mid - 1
        
        # After the loop, left and right will be equal, and the peak will be found
        return left
