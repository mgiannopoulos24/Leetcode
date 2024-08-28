#include <stdio.h>
#include <string.h>

// Function to convert a Roman numeral to an integer
int romanToInt(const char* s) {
    int total = 0;
    int length = strlen(s);
    
    // Loop through the string from left to right
    for (int i = 0; i < length; i++) {
        char current = s[i];
        char next = (i + 1 < length) ? s[i + 1] : '\0';
        
        // Determine the value of the current character
        int currentValue;
        switch (current) {
            case 'I': currentValue = 1; break;
            case 'V': currentValue = 5; break;
            case 'X': currentValue = 10; break;
            case 'L': currentValue = 50; break;
            case 'C': currentValue = 100; break;
            case 'D': currentValue = 500; break;
            case 'M': currentValue = 1000; break;
            default: currentValue = 0; // Invalid character
        }
        
        // Determine the value of the next character
        int nextValue;
        switch (next) {
            case 'I': nextValue = 1; break;
            case 'V': nextValue = 5; break;
            case 'X': nextValue = 10; break;
            case 'L': nextValue = 50; break;
            case 'C': nextValue = 100; break;
            case 'D': nextValue = 500; break;
            case 'M': nextValue = 1000; break;
            default: nextValue = 0; // Invalid character
        }
        
        // Apply the subtraction rule if needed
        if (currentValue < nextValue) {
            total -= currentValue;
        } else {
            total += currentValue;
        }
    }

    return total;
}