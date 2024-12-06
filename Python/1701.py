class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_waiting_time = 0
        current_time = 0
        
        for arrival, time in customers:
            # Update current_time based on whether the chef is idle or not
            current_time = max(current_time, arrival)
            # Chef finishes at current_time + time
            finish_time = current_time + time
            # Calculate the waiting time for this customer
            waiting_time = finish_time - arrival
            # Add to the total waiting time
            total_waiting_time += waiting_time
            # Update the current_time to when the chef finishes this customer's order
            current_time = finish_time
        
        # Return the average waiting time
        return total_waiting_time / len(customers)
