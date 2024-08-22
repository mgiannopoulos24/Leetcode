class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return "";
        }

        int start = 0, maxLen = 1;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            // Check for odd-length palindromes (centered at i)
            int[] len1 = expandAroundCenter(s, i, i);
            // Check for even-length palindromes (centered between i and i+1)
            int[] len2 = expandAroundCenter(s, i, i + 1);

            // Update the maximum length palindrome if necessary
            if (len1[1] - len1[0] > maxLen) {
                start = len1[0];
                maxLen = len1[1] - len1[0];
            }
            if (len2[1] - len2[0] > maxLen) {
                start = len2[0];
                maxLen = len2[1] - len2[0];
            }
        }

        return s.substring(start, start + maxLen);
    }

    // Helper function to expand around the center and return the bounds of the palindrome
    private int[] expandAroundCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        // Return the start and end indices of the palindrome
        return new int[] {left + 1, right};
    }
}