class Solution {
    func convert(_ s: String, _ numRows: Int) -> String {
        let length = s.count
        if numRows == 1 || numRows >= length {
            return s
        }
        
        // Initialize an array of empty strings for each row
        var rows = [String](repeating: "", count: numRows)
        var currentRow = 0
        var goingDown = false
        
        // Traverse each character in the string
        for char in s {
            rows[currentRow].append(char)
            
            // Change direction if we're at the top or bottom row
            if currentRow == 0 || currentRow == numRows - 1 {
                goingDown.toggle()
            }
            
            // Move to the next row
            currentRow += goingDown ? 1 : -1
        }
        
        // Concatenate all rows to get the final result
        return rows.joined()
    }
}
