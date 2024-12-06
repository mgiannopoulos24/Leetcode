class Solution:
    def maxValue(self, n: str, x: int) -> str:
        x = str(x)

        if n[0] != '-':  # Positive number
            for i in range(len(n)):
                if n[i] < x:
                    return n[:i] + x + n[i:]
            return n + x
        else:  # Negative number
            for i in range(1, len(n)):
                if n[i] > x:
                    return n[:i] + x + n[i:]
            return n + x
