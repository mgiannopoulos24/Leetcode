class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        # Find the common prefix
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        # Shift back to restore the common bits to their original position
        return left << shift
