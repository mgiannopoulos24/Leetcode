class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        waiting_customers = 0
        total_boarded = 0
        max_profit = -1
        max_rotation = -1
        current_profit = 0
        rotations = 0
        
        for i in range(len(customers)):
            # Add newly arrived customers to waiting queue
            waiting_customers += customers[i]
            
            # Calculate how many can board in this rotation
            board_now = min(waiting_customers, 4)
            total_boarded += board_now
            waiting_customers -= board_now
            
            # Increment the rotation count
            rotations += 1
            
            # Calculate current profit
            current_profit = total_boarded * boardingCost - rotations * runningCost
            
            # Update max profit and rotation if current profit is higher
            if current_profit > max_profit:
                max_profit = current_profit
                max_rotation = rotations
        
        # Handle remaining waiting customers after processing the array
        while waiting_customers > 0:
            board_now = min(waiting_customers, 4)
            total_boarded += board_now
            waiting_customers -= board_now
            
            # Increment the rotation count
            rotations += 1
            
            # Calculate current profit
            current_profit = total_boarded * boardingCost - rotations * runningCost
            
            # Update max profit and rotation if current profit is higher
            if current_profit > max_profit:
                max_profit = current_profit
                max_rotation = rotations
        
        # If no positive profit was ever achieved, return -1
        return max_rotation if max_profit > 0 else -1
