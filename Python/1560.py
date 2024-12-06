class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # If start <= end, the most visited sectors are simply from start to end
        if rounds[0] <= rounds[-1]:
            result = list(range(rounds[0], rounds[-1] + 1))
        else:
            # If start > end, the most visited sectors are from start to n, then from 1 to end
            result = list(range(rounds[0], n + 1)) + list(range(1, rounds[-1] + 1))
        
        # Return the result sorted in ascending order
        return sorted(result)
