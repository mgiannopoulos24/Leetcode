#include <unordered_map>
#include <string>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        std::unordered_map<char, int> charMap;
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < s.length(); ++right) {
            char currentChar = s[right];

            // If the character is found in the map and it's within the current window
            if (charMap.find(currentChar) != charMap.end() && charMap[currentChar] >= left) {
                // Move the left pointer to the right of the last occurrence of currentChar
                left = charMap[currentChar] + 1;
            }

            // Update the last seen index of the current character
            charMap[currentChar] = right;

            // Calculate the length of the current substring and update maxLength
            maxLength = std::max(maxLength, right - left + 1);
        }

        return maxLength;
    }
};
