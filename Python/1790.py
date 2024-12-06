class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Step 1: Find indices where s1 and s2 differ
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
        
        # Step 2: Evaluate based on number of differences
        if len(diff) == 0:
            return True  # Strings are already equal
        elif len(diff) == 2:
            # Check if swapping makes the strings equal
            i, j = diff
            return s1[i] == s2[j] and s1[j] == s2[i]
        else:
            return False  # More than two differences
