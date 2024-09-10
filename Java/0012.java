class Solution {
    public String intToRoman(int num) {
        // Define the symbols and their corresponding values
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        StringBuilder result = new StringBuilder();
        
        // Iterate over the values and symbols
        for (int i = 0; i < values.length; i++) {
            // Determine how many times the current value fits into num
            while (num >= values[i]) {
                // Append the corresponding symbol
                result.append(symbols[i]);
                // Reduce num by the value
                num -= values[i];
            }
        }
        
        return result.toString();
    }

}
