class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # Calculate x using the derived formula
        if (tomatoSlices - 2 * cheeseSlices) % 2 != 0 or tomatoSlices < 2 * cheeseSlices:
            return []
        
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x
        
        if x >= 0 and y >= 0:
            return [x, y]
        else:
            return []
