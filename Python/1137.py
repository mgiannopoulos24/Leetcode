class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # Initialize the first three numbers
        t0, t1, t2 = 0, 1, 1

        # Compute from T3 to Tn
        for i in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next
        
        return t2
