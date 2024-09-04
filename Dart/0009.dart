class Solution {
  bool isPalindrome(int x) {
    // Negative numbers and numbers ending with zero (but not zero itself) cannot be palindromes.
    if (x < 0 || (x % 10 == 0 && x != 0)) {
      return false;
    }
    
    int original = x;
    int reversed = 0;
    
    while (x > 0) {
      int digit = x % 10; // Get the last digit
      reversed = reversed * 10 + digit; // Append digit to the reversed number
      x ~/= 10; // Remove the last digit from x
    }
    
    return original == reversed; // Check if the original number is the same as the reversed number
  }
}
