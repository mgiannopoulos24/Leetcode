class Solution:
    def countSegments(self, s: str) -> int:
        # Split the string by spaces and filter out any empty segments
        segments = s.strip().split()
        # Return the number of segments
        return len(segments)
