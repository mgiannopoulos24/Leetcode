using System;
using System.Collections.Generic;

public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int n = s.Length;
        int maxLength = 0;
        int left = 0;
        Dictionary<char, int> charMap = new Dictionary<char, int>();

        for (int right = 0; right < n; right++) {
            char currentChar = s[right];

            if (charMap.ContainsKey(currentChar)) {
                // Move the left pointer to the right of the last occurrence of currentChar
                left = Math.Max(charMap[currentChar] + 1, left);
            }

            // Update the last seen index of currentChar
            charMap[currentChar] = right;

            // Calculate the length of the current substring and update maxLength
            maxLength = Math.Max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
