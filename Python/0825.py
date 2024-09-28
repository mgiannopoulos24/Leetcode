from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # Step 1: Use a counter to count how many people are of each age
        age_count = Counter(ages)
        friend_requests = 0
        
        # Step 2: Iterate over possible ages for x and y
        for age_x in age_count:
            for age_y in age_count:
                if age_y <= 0.5 * age_x + 7:  # Condition 1: age[y] <= 0.5 * age[x] + 7
                    continue
                if age_y > age_x:  # Condition 2: age[y] > age[x]
                    continue
                if age_y > 100 and age_x < 100:  # Condition 3: age[y] > 100 and age[x] < 100
                    continue
                
                # Valid friend requests between age_x and age_y
                if age_x == age_y:
                    # If both have the same age, each person can send requests to others of the same age
                    friend_requests += age_count[age_x] * (age_count[age_x] - 1)
                else:
                    friend_requests += age_count[age_x] * age_count[age_y]
        
        return friend_requests
