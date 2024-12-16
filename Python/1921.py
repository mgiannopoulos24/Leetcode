class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Step 1: Calculate the time it takes for each monster to reach the city
        n = len(dist)
        times = []
        for i in range(n):
            # Calculate the time to reach the city for monster i
            time_to_reach = dist[i] / speed[i]
            times.append(time_to_reach)
        
        # Step 2: Sort the times in ascending order
        times.sort()
        
        # Step 3: Try to eliminate as many monsters as possible
        for i in range(n):
            # Check if we can eliminate this monster before it reaches the city
            if times[i] <= i:
                return i  # If the time to reach is less than or equal to i, we lose.
        
        # If we can eliminate all monsters, return n
        return n
