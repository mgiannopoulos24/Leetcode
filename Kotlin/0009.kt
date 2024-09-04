class Solution {
    fun isPalindrome(x: Int): Boolean {
        // Negative numbers and numbers ending in zero (except zero itself) cannot be palindromes.
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false
        }
        
        var original = x
        var reversed = 0
        
        // Reverse the number
        var num = x
        while (num > 0) {
            val digit = num % 10 // Get the last digit
            reversed = reversed * 10 + digit // Build the reversed number
            num /= 10 // Remove the last digit from num
        }
        
        // Compare the reversed number with the original number
        return original == reversed
    }
}
