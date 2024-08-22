class Solution {
    fun longestPalindrome(s: String): String {
        if (s.isEmpty()) {
            return ""
        }

        var start = 0
        var maxLen = 1

        for (i in s.indices) {
            // Find the longest palindrome centered at i (odd length)
            val (l1, r1) = expandAroundCenter(s, i, i)
            // Find the longest palindrome centered between i and i + 1 (even length)
            val (l2, r2) = expandAroundCenter(s, i, i + 1)

            // Update the maximum length palindrome if necessary
            if (r1 - l1 > maxLen) {
                start = l1
                maxLen = r1 - l1
            }
            if (r2 - l2 > maxLen) {
                start = l2
                maxLen = r2 - l2
            }
        }

        return s.substring(start, start + maxLen)
    }

    // Helper function to expand around the center and return the bounds of the palindrome
    private fun expandAroundCenter(s: String, left: Int, right: Int): Pair<Int, Int> {
        var l = left
        var r = right
        while (l >= 0 && r < s.length && s[l] == s[r]) {
            l--
            r++
        }
        // Return the start and end indices of the palindrome
        return Pair(l + 1, r)
    }
}