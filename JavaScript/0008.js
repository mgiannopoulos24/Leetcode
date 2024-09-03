/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    // Define the 32-bit signed integer boundaries
    const INT_MIN = -2147483648;
    const INT_MAX = 2147483647;
    
    // Trim leading whitespaces
    s = s.trim();
    if (s.length === 0) {
        return 0;
    }
    
    // Initialize the sign
    let sign = 1;
    let index = 0;
    
    // Check for the sign
    if (s[index] === '-') {
        sign = -1;
        index++;
    } else if (s[index] === '+') {
        index++;
    }
    
    // Initialize the result variable
    let result = 0;
    
    // Process the digits
    while (index < s.length && s[index] >= '0' && s[index] <= '9') {
        let digit = s[index] - '0';
        
        // Check for overflow before updating result
        if (result > (INT_MAX - digit) / 10) {
            return sign === 1 ? INT_MAX : INT_MIN;
        }
        
        result = result * 10 + digit;
        index++;
    }
    
    return sign * result;
};