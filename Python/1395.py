class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total_teams = 0
        
        # Iterate through each soldier as the middle soldier j
        for j in range(1, n - 1):
            # Count how many soldiers are less than and greater than rating[j] to the left and right
            less_left = greater_left = less_right = greater_right = 0
            
            # Count how many soldiers are smaller/larger than rating[j] on the left
            for i in range(j):
                if rating[i] < rating[j]:
                    less_left += 1
                elif rating[i] > rating[j]:
                    greater_left += 1
            
            # Count how many soldiers are smaller/larger than rating[j] on the right
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    less_right += 1
                elif rating[k] > rating[j]:
                    greater_right += 1
            
            # Form increasing teams: (i, j, k) where rating[i] < rating[j] < rating[k]
            total_teams += less_left * greater_right
            
            # Form decreasing teams: (i, j, k) where rating[i] > rating[j] > rating[k]
            total_teams += greater_left * less_right
        
        return total_teams
