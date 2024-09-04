func isPalindrome(x int) bool {
    // Negative numbers and numbers ending in zero (but not zero itself) cannot be palindromes.
    if x < 0 || (x % 10 == 0 && x != 0) {
        return false
    }
    
    original := x
    reversed := 0
    
    // Reverse the number
    for x > 0 {
        digit := x % 10 // Get the last digit
        reversed = reversed * 10 + digit // Build the reversed number
        x /= 10 // Remove the last digit from x
    }
    
    // Compare the reversed number with the original number
    return original == reversed
}
