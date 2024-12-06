class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        
        length = [0] * (n + 2)  # To store the length of contiguous 1's, we pad with 0 at both ends
        count_m = 0  # To keep track of how many groups of length m exist
        result = -1  # To store the last step at which we have a group of size m
        
        # Iterate through the array `arr`
        for step, pos in enumerate(arr):
            left = length[pos - 1]  # Length of 1's group to the left of pos
            right = length[pos + 1]  # Length of 1's group to the right of pos
            
            # The new length of the group after setting pos to 1
            new_length = left + right + 1
            
            # Update the lengths at the boundaries
            length[pos - left] = new_length  # Update the left boundary
            length[pos + right] = new_length  # Update the right boundary
            
            # Update the count of groups of size `m`
            if left == m:
                count_m -= 1
            if right == m:
                count_m -= 1
            if new_length == m:
                count_m += 1
            
            # If there are any groups of size m, update the result
            if count_m > 0:
                result = step + 1
        
        return result
