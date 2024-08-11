#include <stdbool.h>
#include <limits.h>

bool isPalindrome(int x) {
    // Negative numbers are not palindromes
    if (x < 0) return false;

    // Variables for reversed number and original number
    int original = x;
    int reversed = 0;

    // Reverse the number
    while (x > 0) {
        int digit = x % 10;
        
        // Check for potential overflow before multiplying and adding
        if (reversed > (INT_MAX - digit) / 10) {
            return false; // Overflow would occur
        }

        reversed = reversed * 10 + digit;
        x /= 10;
    }

    // Check if the reversed number is equal to the original number
    return original == reversed;
}
