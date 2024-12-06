class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # Maximum time for ants moving to the left
        max_left_time = max(left) if left else 0
        
        # Maximum time for ants moving to the right
        max_right_time = max(n - r for r in right) if right else 0
        
        # The last ant to fall off is either from the left or right
        return max(max_left_time, max_right_time)
