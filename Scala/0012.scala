object Solution {
  def intToRoman(num: Int): String = {
    // Define the Roman numerals and their corresponding values
    val romanMap = List(
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I")
    )

    // Initialize result as an empty string
    var result = new StringBuilder
    var remaining = num

    // Iterate through the list of values and symbols
    for ((value, symbol) <- romanMap) {
      // While the remaining number is greater than or equal to the value
      while (remaining >= value) {
        result.append(symbol)
        remaining -= value
      }
    }

    // Convert StringBuilder to String and return the result
    result.toString
  }
}
