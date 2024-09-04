public class Solution {
    public bool IsPalindrome(int x) {
        // Handle special cases
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        
        int original = x;
        int reversed = 0;
        
        // Reverse the integer
        while (x > 0) {
            int digit = x % 10;
            reversed = reversed * 10 + digit;
            x = x / 10;
        }
        
        // Compare reversed with the original number
        return original == reversed;
    }
}
