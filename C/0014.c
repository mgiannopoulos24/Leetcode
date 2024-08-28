#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) {
        return "";
    }
    
    // Take the first string as the reference
    char* firstStr = strs[0];
    int firstStrLen = strlen(firstStr);
    
    // Iterate through each character of the first string
    for (int i = 0; i < firstStrLen; i++) {
        char currentChar = firstStr[i];
        
        // Compare the current character with the corresponding character in all other strings
        for (int j = 1; j < strsSize; j++) {
            // If the current string is shorter or the character at this position doesn't match
            if (i >= strlen(strs[j]) || strs[j][i] != currentChar) {
                // Allocate space for the prefix string
                char* prefix = (char*)malloc((i + 1) * sizeof(char));
                if (prefix == NULL) {
                    return NULL; // Memory allocation failed
                }
                // Copy the prefix to the newly allocated memory
                strncpy(prefix, firstStr, i);
                prefix[i] = '\0'; // Null-terminate the prefix string
                return prefix;
            }
        }
    }
    
    // If no mismatch is found, the entire first string is the common prefix
    char* prefix = (char*)malloc((firstStrLen + 1) * sizeof(char));
    if (prefix == NULL) {
        return NULL; // Memory allocation failed
    }
    strcpy(prefix, firstStr);
    return prefix;
}
