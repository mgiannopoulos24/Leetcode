class Solution {
    fun isMatch(s: String, p: String): Boolean {
        val m = s.length
        val n = p.length
        
        // Create a DP table with (m+1) x (n+1) dimensions
        val dp = Array(m + 1) { BooleanArray(n + 1) }
        
        // Base case: empty string matches empty pattern
        dp[0][0] = true
        
        // Initialize DP table for patterns that can match an empty string
        for (j in 1..n) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2]
            }
        }
        
        // Fill the DP table
        for (i in 1..m) {
            for (j in 1..n) {
                if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
                    dp[i][j] = dp[i - 1][j - 1]
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (p[j - 2] == s[i - 1] || p[j - 2] == '.'))
                }
            }
        }
        
        return dp[m][n]
    }
}