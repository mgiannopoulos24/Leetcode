class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Sort the unique elements of the array
        sorted_unique = sorted(set(arr))
        
        # Step 2: Create a dictionary that maps each element to its rank
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
        
        # Step 3: Replace each element in the original array with its rank
        return [rank_map[value] for value in arr]
