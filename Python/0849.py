class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_dist = 0
        last_person = -1
        
        # Traverse the seats to find the maximum distance between occupied seats
        for i in range(n):
            if seats[i] == 1:
                if last_person == -1:
                    # Special case for seats before the first person
                    max_dist = i
                else:
                    # Compute distance between two occupied seats
                    max_dist = max(max_dist, (i - last_person) // 2)
                last_person = i
        
        # Special case for seats after the last person
        max_dist = max(max_dist, n - 1 - last_person)
        
        return max_dist
