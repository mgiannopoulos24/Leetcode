from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize two pointers for the sliding window
        left, right = 0, len(arr) - k
        
        # Find the best window of k closest elements
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        # Extract the k closest elements
        return arr[left:left + k]
