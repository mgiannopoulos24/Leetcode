package main

import "fmt"

func isMatch(s string, p string) bool {
    m, n := len(s), len(p)

    // Create a DP table with (m+1) x (n+1) dimensions
    dp := make([][]bool, m+1)
    for i := range dp {
        dp[i] = make([]bool, n+1)
    }

    // Base case: empty string matches empty pattern
    dp[0][0] = true

    // Initialize the DP table for patterns that can match an empty string
    for j := 1; j <= n; j++ {
        if p[j-1] == '*' {
            dp[0][j] = dp[0][j-2]
        }
    }

    // Fill the DP table
    for i := 1; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if p[j-1] == s[i-1] || p[j-1] == '.' {
                dp[i][j] = dp[i-1][j-1]
            } else if p[j-1] == '*' {
                dp[i][j] = dp[i][j-2] || (dp[i-1][j] && (p[j-2] == s[i-1] || p[j-2] == '.'))
            }
        }
    }

    return dp[m][n]
}

