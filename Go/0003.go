func lengthOfLongestSubstring(s string) int {
    // Create a map to store the last index of each character
    charIndexMap := make(map[rune]int)
    
    maxLen := 0
    start := 0 // Start index of the current substring
    
    for i, char := range s {
        // If the character is already in the map and its index is within the current window
        if lastIndex, found := charIndexMap[char]; found && lastIndex >= start {
            // Move the start index to one position after the last index of the current character
            start = lastIndex + 1
        }
        
        // Update the last index of the current character
        charIndexMap[char] = i
        
        // Calculate the length of the current window and update maxLen if needed
        currentLen := i - start + 1
        if currentLen > maxLen {
            maxLen = currentLen
        }
    }
    
    return maxLen
}