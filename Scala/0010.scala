object Solution {
  def isMatch(s: String, p: String): Boolean = {
    val m = s.length
    val n = p.length

    // dp[i][j] will be true if s[0...i-1] matches p[0...j-1]
    val dp = Array.ofDim[Boolean](m + 1, n + 1)
    
    // An empty pattern matches an empty string
    dp(0)(0) = true

    // Initialize dp for patterns like a*, a*b*, a*b*c* which can match an empty string
    for (j <- 1 to n) {
      if (p(j - 1) == '*') {
        dp(0)(j) = dp(0)(j - 2)
      }
    }

    // Fill the dp table
    for (i <- 1 to m) {
      for (j <- 1 to n) {
        if (p(j - 1) == '.' || p(j - 1) == s(i - 1)) {
          dp(i)(j) = dp(i - 1)(j - 1)
        } else if (p(j - 1) == '*') {
          dp(i)(j) = dp(i)(j - 2) || (dp(i - 1)(j) && (p(j - 2) == s(i - 1) || p(j - 2) == '.'))
        }
      }
    }

    dp(m)(n)
  }
}
