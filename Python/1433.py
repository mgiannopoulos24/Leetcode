class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        # Sort both strings
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        
        # Check if s1_sorted can break s2_sorted
        can_s1_break_s2 = all(c1 >= c2 for c1, c2 in zip(s1_sorted, s2_sorted))
        
        # Check if s2_sorted can break s1_sorted
        can_s2_break_s1 = all(c2 >= c1 for c1, c2 in zip(s1_sorted, s2_sorted))
        
        # Return True if either s1 can break s2 or s2 can break s1
        return can_s1_break_s2 or can_s2_break_s1