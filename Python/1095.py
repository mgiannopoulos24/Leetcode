# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Helper function to find the peak of the mountain array
        def find_peak(mountain_arr):
            low, high = 0, mountain_arr.length() - 1
            while low < high:
                mid = (low + high) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    low = mid + 1
                else:
                    high = mid
            return low
        
        # Helper function for binary search on increasing part
        def binary_search_increasing(mountain_arr, target, low, high):
            while low <= high:
                mid = (low + high) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        # Helper function for binary search on decreasing part
        def binary_search_decreasing(mountain_arr, target, low, high):
            while low <= high:
                mid = (low + high) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                elif mid_val > target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        # Step 1: Find the peak of the mountain array
        peak = find_peak(mountain_arr)
        
        # Step 2: Search for the target in the increasing part (0 to peak)
        result = binary_search_increasing(mountain_arr, target, 0, peak)
        if result != -1:
            return result
        
        # Step 3: Search for the target in the decreasing part (peak + 1 to end)
        return binary_search_decreasing(mountain_arr, target, peak + 1, mountain_arr.length() - 1)