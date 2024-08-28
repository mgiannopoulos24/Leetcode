/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper function to perform recursive backtracking
void backtrack(char* current, int pos, int open, int close, int n, char*** result, int* returnSize) {
    if (pos == 2 * n) {
        current[pos] = '\0'; // Null-terminate the string
        (*result)[*returnSize] = strdup(current); // Duplicate the current string
        (*returnSize)++;
        return;
    }
    
    if (open < n) {
        current[pos] = '(';
        backtrack(current, pos + 1, open + 1, close, n, result, returnSize);
    }
    
    if (close < open) {
        current[pos] = ')';
        backtrack(current, pos + 1, open, close + 1, n, result, returnSize);
    }
}

char** generateParenthesis(int n, int* returnSize) {
    // Allocate memory for the result array
    char** result = (char**)malloc(sizeof(char*) * 10000);
    *returnSize = 0;
    
    // Allocate memory for the current string
    char* current = (char*)malloc(sizeof(char) * (2 * n + 1));
    
    backtrack(current, 0, 0, 0, n, &result, returnSize);

    // Free the current string memory
    free(current);
    return result;
}

// Function to free the result array
void freeResult(char** result, int size) {
    for (int i = 0; i < size; i++) {
        free(result[i]);
    }
    free(result);
}
