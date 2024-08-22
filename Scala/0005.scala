object Solution {
    def longestPalindrome(s: String): String = {
        if (s.isEmpty) return ""

        var start = 0
        var maxLen = 1

        def expandAroundCenter(left: Int, right: Int): (Int, Int) = {
            var l = left
            var r = right
            while (l >= 0 && r < s.length && s(l) == s(r)) {
                l -= 1
                r += 1
            }
            (l + 1, r)
        }

        for (i <- s.indices) {
            // Odd-length palindromes centered at i
            val (l1, r1) = expandAroundCenter(i, i)
            // Even-length palindromes centered between i and i + 1
            val (l2, r2) = expandAroundCenter(i, i + 1)

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

        s.substring(start, start + maxLen)
    }
}