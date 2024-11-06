class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        answer = [0] * (n + 1)
        
        # Apply the difference array technique
        for first, last, seats in bookings:
            answer[first - 1] += seats
            if last < n:
                answer[last] -= seats
        
        # Compute the prefix sum to get the actual number of seats for each flight
        for i in range(1, n):
            answer[i] += answer[i - 1]
        
        return answer[:n]  # Return only the first n elements
