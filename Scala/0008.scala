object Solution {
  def myAtoi(s: String): Int = {
    val maxInt = 2147483647
    val minInt = -2147483648

    // Step 1: Ignore leading whitespace
    var index = 0
    var n = s.length
    while (index < n && s(index) == ' ') {
      index += 1
    }

    if (index == n) return 0  // If all spaces, return 0

    // Step 2: Check the sign
    var sign = 1
    if (index < n && (s(index) == '-' || s(index) == '+')) {
      if (s(index) == '-') sign = -1
      index += 1
    }

    // Step 3: Convert the number
    var result = 0
    while (index < n && s(index).isDigit) {
      val digit = s(index) - '0'
      // Check for overflow before multiplying and adding
      if (result > (maxInt - digit) / 10) {
        return if (sign == 1) maxInt else minInt
      }
      result = result * 10 + digit
      index += 1
    }

    sign * result
  }
}
