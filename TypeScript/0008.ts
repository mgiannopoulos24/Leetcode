function myAtoi(s: string): number {
    // Define the 32-bit signed integer boundaries
    const INT_MIN = -2147483648;
    const INT_MAX = 2147483647;
    
    // Trim leading and trailing whitespaces
    s = s.trim();
    
    // Check for empty string
    if (s.length === 0) {
        return 0;
    }
    
    // Initialize variables
    let index = 0;
    let sign = 1;
    let result = 0;
    
    // Check the sign
    if (s[index] === '-') {
        sign = -1;
        index++;
    } else if (s[index] === '+') {
        index++;
    }
    
    // Process the digits
    while (index < s.length && s[index].match(/[0-9]/)) {
        const digit = Number(s[index]);
        
        // Check for overflow before updating result
        if (result > (INT_MAX - digit) / 10) {
            return sign === 1 ? INT_MAX : INT_MIN;
        }
        
        result = result * 10 + digit;
        index++;
    }
    
    return sign * result;
}