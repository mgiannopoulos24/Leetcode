class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        let characters = Array(s)  // Convert the string to an array of characters
        var charSet = Set<Character>()  // This set will keep track of characters in the current window
        var left = 0  // Left pointer of the sliding window
        var maxLength = 0  // Maximum length of substring without repeating characters
        
        for right in 0..<characters.count {
            // Move the right pointer and include the new character in the window
            while charSet.contains(characters[right]) {
                // Remove characters from the left side of the window until the current character is unique
                charSet.remove(characters[left])
                left += 1
            }
            charSet.insert(characters[right])
            maxLength = max(maxLength, right - left + 1)  // Update the maximum length
        }
        
        return maxLength
    }
}
