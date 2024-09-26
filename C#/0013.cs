public class Solution {
    public int RomanToInt(string s) {
        // Dictionary to store Roman numeral values
        Dictionary<char, int> romanMap = new Dictionary<char, int>() {
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

        // Loop through each character in the string
        for (int i = s.Length - 1; i >= 0; i--) {
            char currentChar = s[i];
            int currentValue = romanMap[currentChar];

            // If the current value is less than the previous one, subtract it
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
}
