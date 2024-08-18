/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let start = 0;
    let maxLength = 0;
    let charSet = new Set();

    for (let end = 0; end < s.length; end++) {
        // If character is in the set, remove characters from start until it's removed
        while (charSet.has(s[end])) {
            charSet.delete(s[start]);
            start++;
        }
        
        // Add the current character to the set
        charSet.add(s[end]);
        
        // Update the maximum length found
        maxLength = Math.max(maxLength, end - start + 1);
    }
    
    return maxLength;
};