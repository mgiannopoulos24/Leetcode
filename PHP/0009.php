class Solution {

/**
 * @param Integer $x
 * @return Boolean
 */
function isPalindrome($x) {
    // Negative numbers and numbers ending in zero (except zero itself) cannot be palindromes.
    if ($x < 0 || ($x % 10 == 0 && $x != 0)) {
        return false;
    }
    
    $original = $x;
    $reversed = 0;
    
    // Reverse the number
    while ($x > 0) {
        $digit = $x % 10; // Get the last digit
        $reversed = $reversed * 10 + $digit; // Build the reversed number
        $x = intdiv($x, 10); // Remove the last digit from $x
    }
    
    // Compare the reversed number with the original number
    return $original == $reversed;
}
}
