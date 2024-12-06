class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        from collections import defaultdict
        
        # Function to calculate sum of digits of a number
        def digit_sum(num):
            return sum(int(d) for d in str(num))
        
        # Dictionary to count balls in each box
        box_counts = defaultdict(int)
        
        # Iterate through each ball number from lowLimit to highLimit
        for ball_number in range(lowLimit, highLimit + 1):
            box_number = digit_sum(ball_number)
            box_counts[box_number] += 1
            
        # Find the maximum count of balls in any box
        return max(box_counts.values())
