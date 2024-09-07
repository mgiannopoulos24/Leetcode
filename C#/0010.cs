public class Solution {
    public bool IsMatch(string s, string p) {
        int m = s.Length;
        int n = p.Length;
        bool[,] dp = new bool[m + 1, n + 1];

        // Base case: empty pattern matches empty string
        dp[0, 0] = true;

        // Handle patterns like a*, a*b*, a*b*c* where they can match empty string
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0, j] = dp[0, j - 2];
            }
        }

        // Fill the dp table
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                    dp[i, j] = dp[i - 1, j - 1];
                } else if (p[j - 1] == '*') {
                    // Zero occurrence or more occurrences of the preceding character
                    dp[i, j] = dp[i, j - 2] || (p[j - 2] == s[i - 1] || p[j - 2] == '.') && dp[i - 1, j];
                }
            }
        }

        return dp[m, n];
    }
}
