class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        # Initialize the result array to hold the candy distribution
        result = [0] * num_people
        
        # Start distributing candies
        current_candy = 1  # The first candy to be given
        i = 0  # Index for the current person (we'll use i % num_people for cyclic distribution)
        
        while candies > 0:
            # Give the current person either the current_candy or the remaining candies (whichever is smaller)
            result[i % num_people] += min(current_candy, candies)
            
            # Subtract the given candies from the total candies
            candies -= current_candy
            
            # Move to the next person and increment the candy amount to be given
            current_candy += 1
            i += 1
        
        return result
