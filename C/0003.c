#include <stdio.h>
#include <string.h>

int lengthOfLongestSubstring(char* s) {
    // Initialize an array to store the last seen index of each character
    // Considering ASCII, there are 128 possible characters
    int char_index_map[128];
    // Set all indices to -1 to indicate that they haven't been seen
    for (int i = 0; i < 128; i++) {
        char_index_map[i] = -1;
    }
    
    // Initialize the starting index of the current window
    int start = 0;
    // Initialize the maximum length of substring without repeating characters
    int max_length = 0;
    
    // Iterate over the string using the index
    int length = strlen(s);
    for (int index = 0; index < length; index++) {
        char current_char = s[index];
        
        // If the character has been seen and is within the current window
        if (char_index_map[(int)current_char] >= start) {
            // Move the start to the right of the last occurrence of the current character
            start = char_index_map[(int)current_char] + 1;
        }
        
        // Update the last seen index of the current character
        char_index_map[(int)current_char] = index;
        
        // Update the maximum length found
        int current_length = index - start + 1;
        if (current_length > max_length) {
            max_length = current_length;
        }
    }
    
    return max_length;
}
