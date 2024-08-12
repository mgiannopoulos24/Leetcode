#include <stdbool.h>
#include <string.h>

// Helper function for memoization
bool dp(int i, int j, char* s, char* p, int** memo) {
    if (memo[i][j] != -1) {
        return memo[i][j];
    }
    
    bool ans;
    if (j == strlen(p)) {
        ans = (i == strlen(s));
    } else {
        bool first_match = (i < strlen(s) && (p[j] == s[i] || p[j] == '.'));

        if (j + 1 < strlen(p) && p[j + 1] == '*') {
            ans = (dp(i, j + 2, s, p, memo) || (first_match && dp(i + 1, j, s, p, memo)));
        } else {
            ans = first_match && dp(i + 1, j + 1, s, p, memo);
        }
    }
    
    memo[i][j] = ans;
    return ans;
}

bool isMatch(char* s, char* p) {
    int m = strlen(s);
    int n = strlen(p);
    
    // Initialize memoization table
    int** memo = (int**)malloc((m + 1) * sizeof(int*));
    for (int i = 0; i <= m; i++) {
        memo[i] = (int*)malloc((n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) {
            memo[i][j] = -1;  // -1 indicates unvisited state
        }
    }
    
    bool result = dp(0, 0, s, p, memo);
    
    // Free memoization table
    for (int i = 0; i <= m; i++) {
        free(memo[i]);
    }
    free(memo);
    
    return result;
}
