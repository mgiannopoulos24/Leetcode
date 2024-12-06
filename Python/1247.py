class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Count the mismatches
        xy = 0  # Count of s1[i] == 'x' and s2[i] == 'y'
        yx = 0  # Count of s1[i] == 'y' and s2[i] == 'x'
        
        # Traverse both strings
        for i in range(len(s1)):
            if s1[i] == 'x' and s2[i] == 'y':
                xy += 1
            elif s1[i] == 'y' and s2[i] == 'x':
                yx += 1
        
        # Check if the total number of mismatches is odd
        if (xy + yx) % 2 != 0:
            return -1
        
        # Compute the minimum swaps
        # Each pair of `xy` and `yx` mismatches can be resolved by 2 swaps
        return (xy // 2) + (yx // 2) + 2 * (xy % 2)
