// Function to return the longest palindromic substring
func longestPalindrome(s string) string {
	if len(s) == 0 {
		return ""
	}

	start, maxLen := 0, 1
	n := len(s)

	for i := 0; i < n; i++ {
		// Check for odd-length palindromes centered at i
		l1, r1 := expandAroundCenter(s, i, i)
		// Check for even-length palindromes centered between i and i+1
		l2, r2 := expandAroundCenter(s, i, i+1)

		if r1-l1 > maxLen {
			start, maxLen = l1, r1-l1
		}
		if r2-l2 > maxLen {
			start, maxLen = l2, r2-l2
		}
	}

	return s[start : start+maxLen]
}

// Helper function to expand around the center
func expandAroundCenter(s string, left, right int) (int, int) {
	for left >= 0 && right < len(s) && s[left] == s[right] {
		left--
		right++
	}
	// Return the bounds of the palindrome
	return left + 1, right
}