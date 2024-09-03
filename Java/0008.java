class Solution {
    public int myAtoi(String s) {
        // Define the 32-bit signed integer boundaries
        final int INT_MIN = Integer.MIN_VALUE;
        final int INT_MAX = Integer.MAX_VALUE;
        
        // Trim leading whitespaces
        s = s.trim();
        if (s.isEmpty()) {
            return 0;
        }
        
        // Initialize the sign
        int sign = 1;
        int index = 0;
        
        // Check for the sign
        if (s.charAt(index) == '-') {
            sign = -1;
            index++;
        } else if (s.charAt(index) == '+') {
            index++;
        }
        
        // Initialize the result variable
        int result = 0;
        
        // Process the digits
        while (index < s.length() && Character.isDigit(s.charAt(index))) {
            int digit = s.charAt(index) - '0';
            
            // Check for overflow before updating result
            if (result > (INT_MAX - digit) / 10) {
                return (sign == 1) ? INT_MAX : INT_MIN;
            }
            
            result = result * 10 + digit;
            index++;
        }
        
        return sign * result;
    }
    
}