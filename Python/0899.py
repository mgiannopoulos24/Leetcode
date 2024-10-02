class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            # For k == 1, try all rotations of the string and find the smallest
            smallest = s
            for i in range(1, len(s)):
                rotated = s[i:] + s[:i]
                if rotated < smallest:
                    smallest = rotated
            return smallest
        else:
            # For k > 1, simply return the sorted string
            return ''.join(sorted(s))
