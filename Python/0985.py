class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Calculate the initial sum of all even numbers in the nums array
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        # Process each query
        for val, index in queries:
            # If the number at the index is currently even, remove it from even_sum
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            
            # Update the number at the index with the value from the query
            nums[index] += val
            
            # If the updated number at the index is now even, add it to even_sum
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            
            # Append the current even_sum to the result list
            result.append(even_sum)
        
        return result
