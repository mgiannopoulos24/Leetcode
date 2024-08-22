class Solution {

/**
 * @param String $s
 * @return String
 */
function longestPalindrome($s) {
    if (strlen($s) === 0) {
        return "";
    }

    $start = 0;
    $maxLen = 1;
    $length = strlen($s);

    for ($i = 0; $i < $length; $i++) {
        // Find the longest palindrome centered at i (odd length)
        list($l1, $r1) = $this->expandAroundCenter($s, $i, $i);
        // Find the longest palindrome centered between i and i+1 (even length)
        list($l2, $r2) = $this->expandAroundCenter($s, $i, $i + 1);

        // Update the maximum length palindrome if necessary
        if ($r1 - $l1 > $maxLen) {
            $start = $l1;
            $maxLen = $r1 - $l1;
        }
        if ($r2 - $l2 > $maxLen) {
            $start = $l2;
            $maxLen = $r2 - $l2;
        }
    }

    return substr($s, $start, $maxLen);
}

/**
 * Helper function to expand around the center and return the bounds of the palindrome
 * @param String $s
 * @param int $left
 * @param int $right
 * @return array
 */
private function expandAroundCenter($s, $left, $right) {
    $length = strlen($s);
    while ($left >= 0 && $right < $length && $s[$left] === $s[$right]) {
        $left--;
        $right++;
    }
    // Return the start and end indices of the palindrome
    return array($left + 1, $right);
}
}