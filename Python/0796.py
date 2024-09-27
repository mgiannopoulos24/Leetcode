class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # Concatenate s with itself and check if goal is a substring
        return goal in (s + s)
