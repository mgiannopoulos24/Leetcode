class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Helper function to count subarrays with at most `k` odd numbers
        def atMostK(k):
            count = 0
            left = 0
            odd_count = 0  # Number of odd numbers in the current window
            
            # Traverse the array with the right pointer
            for right in range(len(nums)):
                # If the number is odd, increment the odd count
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                # If odd_count exceeds `k`, move the left pointer
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                # The number of subarrays that end at `right` is `right - left + 1`
                count += right - left + 1
            
            return count
        
        # Result is the number of subarrays with at most k odd numbers
        # minus the number of subarrays with at most k-1 odd numbers
        return atMostK(k) - atMostK(k - 1)
