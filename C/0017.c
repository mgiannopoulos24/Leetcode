#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the mapping from digits to letters
const char *digitToChar[8] = {
    "abc",  // for digit '2'
    "def",  // for digit '3'
    "ghi",  // for digit '4'
    "jkl",  // for digit '5'
    "mno",  // for digit '6'
    "pqrs", // for digit '7'
    "tuv",  // for digit '8'
    "wxyz"  // for digit '9'
};

// Helper function for backtracking
void backtrack(char *combination, int index, char *digits, char **result, int *returnSize) {
    if (index == strlen(digits)) {
        result[*returnSize] = strdup(combination);
        (*returnSize)++;
        return;
    }

    int digit = digits[index] - '2';
    const char *letters = digitToChar[digit];
    
    for (int i = 0; letters[i] != '\0'; i++) {
        combination[index] = letters[i];
        backtrack(combination, index + 1, digits, result, returnSize);
    }
}

// Main function to return letter combinations
char** letterCombinations(char* digits, int* returnSize) {
    *returnSize = 0;
    if (strlen(digits) == 0) {
        return NULL;
    }

    int n = strlen(digits);
    int totalCombinations = 1;

    // Calculate total combinations
    for (int i = 0; i < n; i++) {
        int digit = digits[i] - '2';
        totalCombinations *= strlen(digitToChar[digit]);
    }

    // Allocate memory for result
    char **result = (char **)malloc(totalCombinations * sizeof(char *));
    char *combination = (char *)malloc((n + 1) * sizeof(char));
    combination[n] = '\0';

    backtrack(combination, 0, digits, result, returnSize);

    free(combination);
    return result;
}