impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let s = s.as_bytes();
        if s.is_empty() {
            return "".to_string();
        }

        let mut start = 0;
        let mut max_len = 1;

        for i in 0..s.len() {
            // Check for odd-length palindromes (centered at i)
            let (l1, r1) = Self::expand_around_center(s, i, i);
            // Check for even-length palindromes (centered between i and i+1)
            let (l2, r2) = Self::expand_around_center(s, i, i + 1);

            // Update the maximum length palindrome if necessary
            if r1 - l1 > max_len {
                start = l1;
                max_len = r1 - l1;
            }
            if r2 - l2 > max_len {
                start = l2;
                max_len = r2 - l2;
            }
        }

        String::from_utf8(s[start..start + max_len].to_vec()).unwrap_or_default()
    }

    // Helper function to expand around the center and return the bounds of the palindrome
    fn expand_around_center(s: &[u8], mut left: usize, mut right: usize) -> (usize, usize) {
        while left > 0 && right < s.len() && s[left - 1] == s[right] {
            left -= 1;
            right += 1;
        }
        (left, right)
    }
}