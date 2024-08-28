object Solution {
    def letterCombinations(digits: String): List[String] = {
        // Mapping of digits to letters as per the phone keypad
        val digitToLetters = Map(
            '2' -> "abc",
            '3' -> "def",
            '4' -> "ghi",
            '5' -> "jkl",
            '6' -> "mno",
            '7' -> "pqrs",
            '8' -> "tuv",
            '9' -> "wxyz"
        )

        // Initialize result list
        val results = scala.collection.mutable.ListBuffer[String]()

        // Helper function to perform backtracking
        def backtrack(index: Int, path: StringBuilder): Unit = {
            if (index == digits.length) {
                // If we have processed all digits, add the path to results
                results += path.toString
            } else {
                val digit = digits(index)
                val letters = digitToLetters.getOrElse(digit, "")
                for (letter <- letters) {
                    path.append(letter)
                    backtrack(index + 1, path)
                    path.deleteCharAt(path.length - 1) // Backtrack
                }
            }
        }

        if (digits.nonEmpty) {
            backtrack(0, new StringBuilder)
        }

        results.toList
    }
}
