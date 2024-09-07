function isMatch(s: string, p: string): boolean {
    const m = s.length;
    const n = p.length;

    // Create a DP table with (m+1) x (n+1) dimensions
    const dp: boolean[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(false));

    // Base case: empty string matches empty pattern
    dp[0][0] = true;

    // Initialize DP table for patterns that can match an empty string
    for (let j = 1; j <= n; j++) {
        if (p[j - 1] === '*') {
            dp[0][j] = dp[0][j - 2];
        }
    }

    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (p[j - 1] === s[i - 1] || p[j - 1] === '.') {
                dp[i][j] = dp[i - 1][j - 1];
            } else if (p[j - 1] === '*') {
                dp[i][j] = dp[i][j - 2] || (dp[i - 1][j] && (p[j - 2] === s[i - 1] || p[j - 2] === '.'));
            }
        }
    }

    return dp[m][n];
}