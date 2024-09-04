class Solution {
    public boolean isPalindrome(int x) {
        // Negative numbers and numbers ending in zero (except zero itself) cannot be palindromes.
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        
        int original = x;
        int reversed = 0;
        
        // Reverse the number
        while (x > 0) {
            int digit = x % 10; // Get the last digit
            reversed = reversed * 10 + digit; // Build the reversed number
            x /= 10; // Remove the last digit from x
        }
        
        // Compare the reversed number with the original number
        return original == reversed;
    }
}
