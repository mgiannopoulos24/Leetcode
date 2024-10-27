class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Sort the heights to get the expected order
        expected = sorted(heights)
        
        # Count the number of mismatches between heights and expected
        mismatch_count = sum(heights[i] != expected[i] for i in range(len(heights)))
        
        return mismatch_count
