class Solution {
public:
    int romanToInt(string s) {
        // Map to store Roman numeral values
        unordered_map<char, int> romanMap = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        
        int total = 0;
        int prevValue = 0;
        
        // Loop through each character in the string from right to left
        for (int i = s.length() - 1; i >= 0; --i) {
            char currentChar = s[i];
            int currentValue = romanMap[currentChar];
            
            // If the current value is smaller than the previous one, subtract it
            if (currentValue < prevValue) {
                total -= currentValue;
            } 
            // Otherwise, add it
            else {
                total += currentValue;
            }
            
            prevValue = currentValue;
        }
        
        return total;
    }
};