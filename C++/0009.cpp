class Solution {
public:
    bool isPalindrome(int x) {
        // Handle special cases
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        
        int original = x;
        int reversed = 0;

        // Reverse only half of the number
        while (x > reversed) {
            int digit = x % 10;
            reversed = reversed * 10 + digit;
            x /= 10;
        }

        // For odd number of digits, remove the middle digit before comparison
        return x == reversed || x == reversed / 10;
    }
};
