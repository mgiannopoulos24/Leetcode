class Solution {
    func longestPalindrome(_ s: String) -> String {
        let s = Array(s) // Convert String to Array of Characters for easier indexing
        if s.isEmpty {
            return ""
        }
        
        var start = 0
        var maxLen = 1
        
        func expandAroundCenter(_ left: Int, _ right: Int) -> (Int, Int) {
            var l = left
            var r = right
            while l >= 0 && r < s.count && s[l] == s[r] {
                l -= 1
                r += 1
            }
            return (l + 1, r)
        }
        
        for i in 0..<s.count {
            // Odd-length palindromes centered at i
            let (l1, r1) = expandAroundCenter(i, i)
            // Even-length palindromes centered between i and i + 1
            let (l2, r2) = expandAroundCenter(i, i + 1)
            
            // Update the maximum length palindrome if necessary
            if r1 - l1 > maxLen {
                start = l1
                maxLen = r1 - l1
            }
            if r2 - l2 > maxLen {
                start = l2
                maxLen = r2 - l2
            }
        }
        
        return String(s[start..<start + maxLen])
    }
}