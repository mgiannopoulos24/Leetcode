class Solution {
  bool isMatch(String s, String p) {
    int m = s.length;
    int n = p.length;
    
    // Create a DP table with (m+1) x (n+1) dimensions
    List<List<bool>> dp = List.generate(m + 1, (_) => List.filled(n + 1, false));
    
    // Base case: empty pattern matches empty string
    dp[0][0] = true;
    
    // Initialize DP table for patterns with '*' that can match an empty string
    for (int j = 1; j <= n; ++j) {
      if (p[j - 1] == '*') {
        dp[0][j] = dp[0][j - 2];
      }
    }
    
    // Fill the DP table
    for (int i = 1; i <= m; ++i) {
      for (int j = 1; j <= n; ++j) {
        if (p[j - 1] == s[i - 1] || p[j - 1] == '.') {
          dp[i][j] = dp[i - 1][j - 1];
        } else if (p[j - 1] == '*') {
          // '*' can match zero or more of the preceding element
          dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (p[j - 2] == s[i - 1] || p[j - 2] == '.'));
        }
      }
    }
    
    return dp[m][n];
  }
}
