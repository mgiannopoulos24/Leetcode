class Solution {

/**
 * @param String $s
 * @return Integer
 */
function lengthOfLongestSubstring($s) {
    $n = strlen($s);
    $charMap = []; // Associative array to store the last index of each character
    $maxLength = 0; // Variable to store the maximum length of substring
    $start = 0; // Start index of the sliding window

    for ($end = 0; $end < $n; $end++) {
        $char = $s[$end];
        // If the character is already in the map and its index is within the current window
        if (isset($charMap[$char]) && $charMap[$char] >= $start) {
            // Move the start of the window to the right of the previous index of the current character
            $start = $charMap[$char] + 1;
        }
        // Update the index of the current character
        $charMap[$char] = $end;
        // Calculate the length of the current window and update maxLength if needed
        $maxLength = max($maxLength, $end - $start + 1);
    }

    return $maxLength;
}
}
