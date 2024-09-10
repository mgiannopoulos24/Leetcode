class Solution {
    fun intToRoman(num: Int): String {
        // Define the values and symbols
        val values = intArrayOf(1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        val symbols = arrayOf("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        
        val result = StringBuilder()
        
        var n = num
        
        // Iterate over the values and symbols
        for (i in values.indices) {
            // Determine how many times the current value fits into num
            while (n >= values[i]) {
                // Append the corresponding symbol
                result.append(symbols[i])
                // Reduce num by the value
                n -= values[i]
            }
        }
        
        return result.toString()
    }
}
