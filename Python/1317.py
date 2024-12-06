class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Helper function to check if a number is a No-Zero integer
        def is_no_zero(x):
            return '0' not in str(x)
        
        # Iterate over possible values of a
        for a in range(1, n):
            b = n - a
            if is_no_zero(a) and is_no_zero(b):
                return [a, b]
