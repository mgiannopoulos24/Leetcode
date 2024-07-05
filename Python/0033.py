class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        if n == 0:
            return -1
        
        # Function to find the pivot index
        def find_pivot():
            left, right = 0, n - 1
            
            while left < right:
                mid = left + (right - left) // 2
                
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                elif nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid
            
            return 0
        
        # Function to perform binary search
        def binary_search(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return -1
        
        # Find the pivot index
        pivot = find_pivot()
        
        # Decide which segment to search in
        if pivot == 0 or target < nums[0]:
            return binary_search(pivot, n - 1)
        else:
            return binary_search(0, pivot - 1)
