class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # Step 1: Sort the array in non-increasing order
        nums.sort(reverse=True)
        
        # Step 2: Calculate the total sum of the array
        total_sum = sum(nums)
        subsequence_sum = 0
        subsequence = []
        
        # Step 3: Keep adding elements to the subsequence until its sum is greater than the remaining sum
        for num in nums:
            subsequence_sum += num
            subsequence.append(num)
            # Remaining sum is total_sum - subsequence_sum
            if subsequence_sum > total_sum - subsequence_sum:
                break
        
        # Return the subsequence which is already in non-increasing order
        return subsequence
