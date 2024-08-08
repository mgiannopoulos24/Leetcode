#include <stdlib.h>
#include <string.h>

char* convert(char* s, int numRows) {
    if (numRows == 1) {
        return strdup(s); // No zigzag pattern needed for a single row
    }

    int len = strlen(s);
    char* result = (char*)malloc(len + 1);
    int step = 2 * numRows - 2;
    int idx = 0;

    for (int r = 0; r < numRows; r++) {
        for (int i = r; i < len; i += step) {
            result[idx++] = s[i];
            // Handle the diagonal elements in the zigzag pattern
            int diag = i + step - 2 * r;
            if (r != 0 && r != numRows - 1 && diag < len) {
                result[idx++] = s[diag];
            }
        }
    }

    result[idx] = '\0'; // Null-terminate the result string
    return result;
}
