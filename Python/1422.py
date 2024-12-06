class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')  # Total number of ones in the string
        max_score = 0
        left_zeros = 0
        left_ones = 0
        
        # Iterate over possible split points
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1  # Increment zeros for the left part
            else:
                left_ones += 1  # Increment ones for the left part
                
            # Right ones can be calculated as total_ones - left_ones
            right_ones = total_ones - left_ones
            
            # Calculate score: left_zeros + right_ones
            score = left_zeros + right_ones
            max_score = max(max_score, score)
        
        return max_score