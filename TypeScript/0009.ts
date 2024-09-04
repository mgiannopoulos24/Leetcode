function isPalindrome(x: number): boolean {
    // Handle negative numbers and numbers ending in zero (except zero itself)
    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }
    
    let original = x;
    let reversed = 0;
    
    // Reverse the number
    while (original > 0) {
        let digit = original % 10; // Get the last digit
        reversed = reversed * 10 + digit; // Build the reversed number
        original = Math.floor(original / 10); // Remove the last digit from original
    }
    
    // Compare the reversed number with the original number
    return x === reversed;
}
