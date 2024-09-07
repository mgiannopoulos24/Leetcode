from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Initialize a counter for planted flowers
        i = 0  # Start at the beginning of the flowerbed

        while i < len(flowerbed):
            # Check if the current plot is empty and if the adjacent plots (if they exist) are empty
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                
                # Plant a flower
                flowerbed[i] = 1
                count += 1  # Increment the planted flower counter
                
                if count >= n:
                    return True
                
                # Skip the next plot as we can't plant adjacent flowers
                i += 2
            else:
                # Move to the next plot
                i += 1

        # If after the loop we haven't planted enough flowers, return False
        return count >= n
