object Solution {
    def convert(s: String, numRows: Int): String = {
        if (numRows == 1 || numRows >= s.length) {
            return s
        }

        // Initialize a vector of empty StringBuilder for each row
        val rows = Array.fill(numRows)(new StringBuilder)
        var currentRow = 0
        var goingDown = false

        // Traverse each character in the string
        s.foreach { char =>
            rows(currentRow).append(char)
            
            // Change direction if we're at the top or bottom row
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown
            }

            // Move to the next row
            currentRow += (if (goingDown) 1 else -1)
        }

        // Concatenate all rows to get the final result
        rows.mkString
    }
}
