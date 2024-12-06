class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies any kid currently has
        max_candies = max(candies)
        
        # For each kid, check if their candies + extraCandies would be greater or equal to the maximum candies
        result = [(candy + extraCandies) >= max_candies for candy in candies]
        
        return result
