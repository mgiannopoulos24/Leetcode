class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Step 1: Calculate the total sum of the array
        total_sum = sum(nums)
        
        # Step 2: If the sum is divisible by 3, return the total sum
        if total_sum % 3 == 0:
            return total_sum
        
        # Step 3: Separate numbers into lists based on their remainder when divided by 3
        remainder1 = []
        remainder2 = []
        
        for num in nums:
            if num % 3 == 1:
                remainder1.append(num)
            elif num % 3 == 2:
                remainder2.append(num)
        
        # Step 4: Sort the remainder lists to get the smallest elements
        remainder1.sort()
        remainder2.sort()
        
        # Step 5: Calculate the possible sums by removing the smallest element(s)
        remainder = total_sum % 3
        if remainder == 1:
            # To fix remainder 1, remove either one smallest element from remainder1 or two smallest from remainder2
            option1 = remainder1[0] if remainder1 else float('inf')
            option2 = sum(remainder2[:2]) if len(remainder2) >= 2 else float('inf')
        elif remainder == 2:
            # To fix remainder 2, remove either one smallest element from remainder2 or two smallest from remainder1
            option1 = remainder2[0] if remainder2 else float('inf')
            option2 = sum(remainder1[:2]) if len(remainder1) >= 2 else float('inf')
        
        # Return the total sum minus the smallest option
        return total_sum - min(option1, option2)
