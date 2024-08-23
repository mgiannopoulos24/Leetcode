#include <bits/stdc++.h>  // using GCC/G++

class Solution {
public:
    string convert(string s, int numRows) {
        // Edge case: if only one row or numRows >= length of s
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }
        
        // Create a vector to store strings for each row
        vector<string> rows(numRows);
        int currentRow = 0;
        bool goingDown = false;

        // Traverse each character in the string
        for (char c : s) {
            rows[currentRow] += c;  // Add current character to the current row
            
            // If we are at the top or bottom, reverse the direction
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }

            // Move to the next row based on the direction
            currentRow += goingDown ? 1 : -1;
        }
        
        // Concatenate all rows to form the final string
        string result;
        for (string row : rows) {
            result += row;
        }

        return result;
    }
};
