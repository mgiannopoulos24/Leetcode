class Solution {

/**
 * @param String $s
 * @return Integer
 */
function myAtoi($s) {
    // Define the 32-bit signed integer boundaries
    $INT_MIN = -2147483648;
    $INT_MAX = 2147483647;
    
    // Trim leading whitespace
    $s = trim($s);
    if (strlen($s) === 0) {
        return 0;
    }
    
    // Initialize the sign and result
    $sign = 1;
    $index = 0;
    $result = 0;
    
    // Check for sign
    if ($s[$index] === '-') {
        $sign = -1;
        $index++;
    } else if ($s[$index] === '+') {
        $index++;
    }
    
    // Process the digits
    while ($index < strlen($s) && ctype_digit($s[$index])) {
        $digit = intval($s[$index]);
        
        // Check for overflow before updating result
        if ($result > ($INT_MAX - $digit) / 10) {
            return $sign === 1 ? $INT_MAX : $INT_MIN;
        }
        
        $result = $result * 10 + $digit;
        $index++;
    }
    
    return $sign * $result;
}
}