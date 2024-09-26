class Solution {
    fun romanToInt(s: String): Int {
        // Map to store Roman numeral values
        val romanMap = mapOf(
            'I' to 1,
            'V' to 5,
            'X' to 10,
            'L' to 50,
            'C' to 100,
            'D' to 500,
            'M' to 1000
        )

        var total = 0
        var prevValue = 0

        // Loop through the string from right to left
        for (i in s.length - 1 downTo 0) {
            val currentChar = s[i]
            val currentValue = romanMap[currentChar]!!

            // If the current value is smaller than the previous one, subtract it
            if (currentValue < prevValue) {
                total -= currentValue
            } else {
                total += currentValue
            }

            prevValue = currentValue
        }

        return total
    }
}
