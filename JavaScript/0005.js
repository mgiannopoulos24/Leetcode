/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length === 0) {
        return "";
    }

    let start = 0, maxLen = 1;

    for (let i = 0; i < s.length; i++) {
        // Find the longest palindrome centered at i (odd length)
        let [l1, r1] = expandAroundCenter(s, i, i);
        // Find the longest palindrome centered between i and i+1 (even length)
        let [l2, r2] = expandAroundCenter(s, i, i + 1);

        // Update the maximum length palindrome if necessary
        if (r1 - l1 > maxLen) {
            start = l1;
            maxLen = r1 - l1;
        }
        if (r2 - l2 > maxLen) {
            start = l2;
            maxLen = r2 - l2;
        }
    }

    return s.substring(start, start + maxLen);
};

/**
 * Helper function to expand around the center and return the bounds of the palindrome
 * @param {string} s
 * @param {number} left
 * @param {number} right
 * @return {number[]} The start and end indices of the palindrome
 */
function expandAroundCenter(s, left, right) {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
        left--;
        right++;
    }
    // Return the start and end indices of the palindrome
    return [left + 1, right];
}