import java.util.HashSet;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();
        int left = 0; // Start of the window
        int maxLength = 0; // Result: the length of the longest substring without repeating characters

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);
            
            // If the character is already in the set, remove characters from the set 
            // until the duplicate character is removed
            while (set.contains(currentChar)) {
                set.remove(s.charAt(left));
                left++;
            }

            // Add the current character to the set
            set.add(currentChar);
            
            // Update the maximum length of substring found
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
