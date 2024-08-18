class Solution {
  int lengthOfLongestSubstring(String s) {
    Map<String, int> charMap = {};
    int maxLength = 0;
    int left = 0;

    for (int right = 0; right < s.length; right++) {
      String currentChar = s[right];

      if (charMap.containsKey(currentChar) && charMap[currentChar]! >= left) {
        // Move the left pointer to the right of the last occurrence of currentChar
        left = charMap[currentChar]! + 1;
      }

      // Update the last seen index of the current character
      charMap[currentChar] = right;

      // Calculate the length of the current substring and update maxLength
      maxLength = max(maxLength, right - left + 1);
    }

    return maxLength;
  }
}
