import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # Sort arr2 for efficient searching
        arr2.sort()
        distance_value = 0
        
        # For each element in arr1, find if any element in arr2 is within the range of [arr1[i] - d, arr1[i] + d]
        for num in arr1:
            # Find the position where `num - d` would fit
            left = bisect.bisect_left(arr2, num - d)
            # Check if there is any element in arr2 within the range [num - d, num + d]
            if left < len(arr2) and abs(arr2[left] - num) <= d:
                continue
            # Check if the element right before `left` might be within the range
            if left > 0 and abs(arr2[left - 1] - num) <= d:
                continue
            # If no elements were found within the range, count this element in the result
            distance_value += 1
        
        return distance_value
