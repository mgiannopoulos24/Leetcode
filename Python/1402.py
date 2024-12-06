class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Sort satisfaction in increasing order
        satisfaction.sort()
        
        # Variables to track the maximum like-time coefficient
        total_sum = 0
        current_sum = 0
        
        # Traverse the satisfaction array from the end (most liked dish)
        for i in range(len(satisfaction) - 1, -1, -1):
            current_sum += satisfaction[i]
            # If the current sum is positive, include this dish
            if current_sum > 0:
                total_sum += current_sum
            else:
                break  # Once current_sum becomes non-positive, stop
        
        return total_sum
