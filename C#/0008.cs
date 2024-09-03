public class Solution {
    public int MyAtoi(string s) {
        if (string.IsNullOrWhiteSpace(s)) {
            return 0;
        }

        int index = 0;
        int n = s.Length;
        
        // Step 1: Ignore leading whitespaces
        while (index < n && s[index] == ' ') {
            index++;
        }
        
        // Step 2: Determine the sign
        int sign = 1;
        if (index < n && (s[index] == '-' || s[index] == '+')) {
            sign = (s[index] == '-') ? -1 : 1;
            index++;
        }
        
        // Step 3: Convert the number
        long result = 0;
        while (index < n && char.IsDigit(s[index])) {
            result = result * 10 + (s[index] - '0');
            index++;
            
            // Step 4: Check for overflow
            if (result * sign > int.MaxValue) return int.MaxValue;
            if (result * sign < int.MinValue) return int.MinValue;
        }
        
        // Return the final result
        return (int)(result * sign);
    }
}
