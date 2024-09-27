class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        change = [0] * n
        
        for i in range(n):
            # nums[i] contributes when it's at index <= nums[i]
            # The range of k values where nums[i] contributes to the score:
            
            # Starting from k = (i - nums[i] + 1 + n) % n to k = i
            lose_start = (i - nums[i] + 1 + n) % n  # where it starts to lose points
            change[lose_start] -= 1                 # decrease the score from here
            
            change[i + 1 if i + 1 < n else 0] += 1  # increase the score where it starts contributing
        
        # Now we accumulate the changes and find the best rotation
        max_score = score = 0
        best_k = 0
        
        for k in range(1, n):
            score += change[k]
            if score > max_score:
                max_score = score
                best_k = k
        
        return best_k
