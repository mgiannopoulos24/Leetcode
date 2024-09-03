class Solution {
  int myAtoi(String s) {
    // Step 1: Initialize and trim leading whitespaces
    int index = 0;
    int n = s.length;
    
    // Trim leading whitespaces
    while (index < n && s[index] == ' ') {
      index++;
    }
    
    if (index == n) return 0; // No digits found

    // Step 2: Determine the sign
    int sign = 1;
    if (index < n && (s[index] == '-' || s[index] == '+')) {
      sign = (s[index] == '-') ? -1 : 1;
      index++;
    }

    // Step 3: Convert digits to integer
    int result = 0;
    while (index < n && RegExp(r'\d').hasMatch(s[index])) {
      int digit = s.codeUnitAt(index) - '0'.codeUnitAt(0);
      
      // Step 4: Check for overflow
      if (result > (2147483647 - digit) ~/ 10) {
        return sign == 1 ? 2147483647 : -2147483648;
      }
      
      result = result * 10 + digit;
      index++;
    }

    // Step 5: Return the result with sign
    return sign * result;
  }
}
