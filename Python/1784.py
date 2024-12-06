class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Check if there's a "01" pattern indicating multiple segments of ones
        return "01" not in s
