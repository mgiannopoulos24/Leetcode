/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // Negative numbers and numbers ending in zero (except zero itself) cannot be palindromes.
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }
    
    let original = x;
    let reversed = 0;
    
    // Reverse the number
    while (x > 0) {
        let digit = x % 10; // Get the last digit
        reversed = reversed * 10 + digit; // Build the reversed number
        x = Math.floor(x / 10); // Remove the last digit from x
    }
    
    // Compare the reversed number with the original number
    return original === reversed;
};
