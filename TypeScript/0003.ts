function lengthOfLongestSubstring(s: string): number {
    // Map to store the index of characters
    const charIndexMap: Map<string, number> = new Map();
    let start = 0; // Start index of the current substring
    let maxLength = 0; // Maximum length of substring found

    for (let end = 0; end < s.length; end++) {
        const char = s[end];

        // If the character is already in the map and its index is within the current window
        if (charIndexMap.has(char) && charIndexMap.get(char)! >= start) {
            // Move the start to the right of the last occurrence of the character
            start = charIndexMap.get(char)! + 1;
        }

        // Update or add the character's index in the map
        charIndexMap.set(char, end);

        // Calculate the length of the current substring
        maxLength = Math.max(maxLength, end - start + 1);
    }

    return maxLength;
}
