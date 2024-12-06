class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # Calculate the total even-indexed and odd-indexed sums
        total_even_sum, total_odd_sum = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                total_even_sum += nums[i]
            else:
                total_odd_sum += nums[i]
        
        # Initialize variables for the prefix sums (left side of the array)
        left_even_sum, left_odd_sum = 0, 0
        result = 0
        
        for i in range(len(nums)):
            # Remove current element and recalculate sums
            
            # After removing nums[i], the left side and the right side will change roles
            if i % 2 == 0:
                total_even_sum -= nums[i]
            else:
                total_odd_sum -= nums[i]
            
            # Now check if the sum of even and odd indices are equal after removal
            if left_even_sum + total_odd_sum == left_odd_sum + total_even_sum:
                result += 1
            
            # Update the prefix sums for the next iteration
            if i % 2 == 0:
                left_even_sum += nums[i]
            else:
                left_odd_sum += nums[i]
        
        return result
