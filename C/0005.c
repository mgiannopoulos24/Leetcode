#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Helper function to find the longest palindromic substring centered at left and right
int expandAroundCenter(char* s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < strlen(s) && s[L] == s[R]) {
        L--;
        R++;
    }
    return R - L - 1;
}

char* longestPalindrome(char* s) {
    if (s == NULL || strlen(s) < 1) {
        return "";
    }
    
    int start = 0, end = 0;
    for (int i = 0; i < strlen(s); i++) {
        int len1 = expandAroundCenter(s, i, i);      // Odd length palindrome
        int len2 = expandAroundCenter(s, i, i + 1);  // Even length palindrome
        int len = len1 > len2 ? len1 : len2;
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    
    // Allocate memory for the result substring
    int resultLen = end - start + 1;
    char* result = (char*)malloc(resultLen + 1);
    strncpy(result, s + start, resultLen);
    result[resultLen] = '\0';  // Null-terminate the string
    
    return result;
}
