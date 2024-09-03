class Solution {
    fun myAtoi(s: String): Int {
        // Define the 32-bit signed integer boundaries
        val INT_MIN = Int.MIN_VALUE
        val INT_MAX = Int.MAX_VALUE

        // Trim leading whitespaces
        var trimmed = s.trim()
        if (trimmed.isEmpty()) {
            return 0
        }

        // Initialize the sign and the result
        var sign = 1
        var index = 0
        var result = 0

        // Check for sign
        if (trimmed[index] == '-') {
            sign = -1
            index++
        } else if (trimmed[index] == '+') {
            index++
        }

        // Process the digits
        while (index < trimmed.length && trimmed[index].isDigit()) {
            val digit = trimmed[index] - '0'

            // Check for overflow before updating result
            if (result > (INT_MAX - digit) / 10) {
                return if (sign == 1) INT_MAX else INT_MIN
            }

            result = result * 10 + digit
            index++
        }

        return sign * result
    }
}