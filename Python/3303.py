class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def compute_z_array(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z

        n, m = len(s), len(pattern)
        if m >= n:
            return -1

        # Compute lcp array
        T = pattern + "$" + s
        z = compute_z_array(T)
        lcp = z[m + 1:]

        # Compute lcs array
        s_rev = s[::-1]
        pattern_rev = pattern[::-1]
        T_rev = pattern_rev + "$" + s_rev
        z_rev = compute_z_array(T_rev)
        lcs_rev = z_rev[m + 1:]
        lcs_rev = lcs_rev + [0] * (n - len(lcs_rev))  # Pad if necessary
        lcs = lcs_rev[::-1]

        # Check for valid starting index
        for i in range(n - m + 1):
            left = lcp[i]
            right = lcs[i + m - 1]
            if left + right >= m - 1:
                return i
        return -1
