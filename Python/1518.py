class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles  # Start with the initial bottles
        empty_bottles = numBottles  # Initially all bottles are full
        
        while empty_bottles >= numExchange:
            # Calculate how many new bottles we can get from exchanging
            new_bottles = empty_bottles // numExchange
            # Update total drunk
            total_drunk += new_bottles
            # Calculate remaining empty bottles after exchanging
            empty_bottles = empty_bottles % numExchange + new_bottles
        
        return total_drunk
