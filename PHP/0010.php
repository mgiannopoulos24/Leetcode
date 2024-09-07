class Solution {

/**
 * @param String $s
 * @param String $p
 * @return Boolean
 */
function isMatch($s, $p) {
    $m = strlen($s);
    $n = strlen($p);
    
    // Create a DP table with (m+1) x (n+1) dimensions
    $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, false));
    
    // Base case: empty string matches empty pattern
    $dp[0][0] = true;
    
    // Initialize DP table for patterns that can match an empty string
    for ($j = 1; $j <= $n; $j++) {
        if ($p[$j - 1] == '*') {
            $dp[0][$j] = $dp[0][$j - 2];
        }
    }
    
    // Fill the DP table
    for ($i = 1; $i <= $m; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            if ($p[$j - 1] == $s[$i - 1] || $p[$j - 1] == '.') {
                $dp[$i][$j] = $dp[$i - 1][$j - 1];
            } else if ($p[$j - 1] == '*') {
                $dp[$i][$j] = $dp[$i][$j - 2] || ($dp[$i - 1][$j] && ($p[$j - 2] == $s[$i - 1] || $p[$j - 2] == '.'));
            }
        }
    }
    
    return $dp[$m][$n];
}
}
