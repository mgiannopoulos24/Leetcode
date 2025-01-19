class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # Sort both the seats and students arrays
        seats.sort()
        students.sort()
        
        # Initialize the total number of moves to 0
        total_moves = 0
        
        # Iterate through the sorted arrays and calculate the moves
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
        
        return total_moves