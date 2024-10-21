class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        # Precompute factorials up to 10
        factorial = [1] * 11
        for i in range(1, 11):
            factorial[i] = factorial[i - 1] * i

        def perm(m, n):
            return factorial[m] // factorial[m - n]

        digits = list(map(int, str(N + 1)))
        n = len(digits)
        res = 0

        # Step 1: Count numbers with unique digits of length less than n
        for i in range(1, n):
            res += 9 * perm(9, i - 1)

        # Step 2: Count numbers with unique digits of length n
        used = set()
        for i in range(n):
            d = digits[i]
            for x in range(0 if i else 1, d):
                if x in used:
                    continue
                res += perm(9 - i, n - i - 1)
            if d in used:
                break
            used.add(d)

        # Step 3: Subtract the total unique numbers from N
        return N - res
