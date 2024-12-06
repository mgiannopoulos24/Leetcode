class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0  # Variable to store the maximum length of the subarray with positive product
        pos_len = 0  # Current length of the subarray with positive product
        neg_len = 0  # Current length of the subarray with negative product
        
        for num in nums:
            if num > 0:
                # Positive number increases pos_len, and if neg_len exists, it also increases
                pos_len += 1
                neg_len = neg_len + 1 if neg_len > 0 else 0
            elif num < 0:
                # Negative number swaps pos_len and neg_len
                new_pos_len = neg_len + 1 if neg_len > 0 else 0
                new_neg_len = pos_len + 1
                pos_len, neg_len = new_pos_len, new_neg_len
            else:
                # Zero resets both pos_len and neg_len
                pos_len = 0
                neg_len = 0
            
            # Update the maximum length of positive subarray
            max_len = max(max_len, pos_len)
        
        return max_len
