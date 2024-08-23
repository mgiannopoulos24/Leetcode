class Solution {
    fun convert(s: String, numRows: Int): String {
        // Edge case: if numRows is 1 or greater than or equal to length of s
        if (numRows == 1 || numRows >= s.length) {
            return s
        }
        
        // Initialize an array of empty strings for each row
        val rows = Array(numRows) { StringBuilder() }
        var currentRow = 0
        var goingDown = false
        
        // Traverse each character in the string
        for (char in s) {
            rows[currentRow].append(char)
            
            // Change direction if we're at the top or bottom row
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown
            }
            
            // Move to the next row
            currentRow += if (goingDown) 1 else -1
        }
        
        // Concatenate all rows to get the final result
        return rows.joinToString(separator = "") { it.toString() }
    }
}
