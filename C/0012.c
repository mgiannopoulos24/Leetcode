#include <stdio.h>
#include <string.h>

// Function to convert integer to Roman numeral
char* intToRoman(int num) {
    // Array of Roman numerals
    char* roman[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    
    // Array of corresponding values
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    
    // Result buffer for storing the Roman numeral
    static char result[20];
    result[0] = '\0'; // Initialize result as an empty string
    
    // Loop through the values
    for (int i = 0; i < 13; i++) {
        // While the number is greater than or equal to the current value
        while (num >= values[i]) {
            // Append the Roman numeral to the result
            strcat(result, roman[i]);
            // Subtract the value from the number
            num -= values[i];
        }
    }
    
    // Return the resulting Roman numeral
    return result;
}