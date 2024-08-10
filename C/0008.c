#include <limits.h> // For INT_MAX and INT_MIN
#include <ctype.h>  // For isdigit() and isspace()

int myAtoi(char* s) {
    int i = 0;
    int sign = 1;
    long result = 0;

    // Step 1: Ignore leading whitespaces
    while (isspace(s[i])) {
        i++;
    }

    // Step 2: Check the sign
    if (s[i] == '-' || s[i] == '+') {
        sign = (s[i] == '-') ? -1 : 1;
        i++;
    }

    // Step 3: Convert digits to integer and handle overflow
    while (isdigit(s[i])) {
        result = result * 10 + (s[i] - '0');

        // Step 4: Handle overflow
        if (result * sign >= INT_MAX) {
            return INT_MAX;
        } else if (result * sign <= INT_MIN) {
            return INT_MIN;
        }

        i++;
    }

    // Return the final result with the correct sign
    return (int)(result * sign);
}
