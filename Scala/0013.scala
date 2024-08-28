object Solution {
  def romanToInt(s: String): Int = {
    // Define a mapping from Roman numerals to their integer values
    val romanMap = Map(
      'I' -> 1,
      'V' -> 5,
      'X' -> 10,
      'L' -> 50,
      'C' -> 100,
      'D' -> 500,
      'M' -> 1000
    )

    // Initialize total sum
    var total = 0
    val length = s.length

    // Iterate through the string
    for (i <- 0 until length) {
      // Get the value of the current numeral
      val current = romanMap(s(i))
      // Get the value of the next numeral (if it exists)
      val next = if (i + 1 < length) romanMap(s(i + 1)) else 0

      // Determine if we should add or subtract the current value
      if (current < next) {
        total -= current
      } else {
        total += current
      }
    }

    total
  }
}
