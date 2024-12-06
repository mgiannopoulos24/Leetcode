class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # Modulo value
        MOD = 10**9 + 7
        
        # Sort the cuts
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Compute the maximum gap in the horizontal cuts
        max_h_gap = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h_gap = max(max_h_gap, horizontalCuts[i] - horizontalCuts[i - 1])
        
        # Compute the maximum gap in the vertical cuts
        max_v_gap = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_v_gap = max(max_v_gap, verticalCuts[i] - verticalCuts[i - 1])
        
        # The maximum area is the product of the largest gaps in both directions
        return (max_h_gap * max_v_gap) % MOD
