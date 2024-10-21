class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        
        # If the total sum is not divisible by 3, we can't partition the array into 3 parts with equal sum
        if total_sum % 3 != 0:
            return False
        
        target = total_sum // 3
        count, current_sum = 0, 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            # Whenever we find a subarray with sum equal to target, we reset the current sum
            if current_sum == target:
                count += 1
                current_sum = 0
                
                # If we found 2 parts and we are not at the last element, then return True
                if count == 2 and i < len(arr) - 1:
                    return True
        
        # If we couldn't find exactly 2 partitions, return False
        return False
