object Solution {
    def generateParenthesis(n: Int): List[String] = {
        // Helper function to perform recursive backtracking
        def backtrack(current: StringBuilder, pos: Int, open: Int, close: Int, n: Int, result: List[String]): List[String] = {
            if (pos == 2 * n) {
                result :+ current.toString() // Add the current combination to the result list
            } else {
                var newResult = result
                if (open < n) {
                    current.append('(')
                    newResult = backtrack(current, pos + 1, open + 1, close, n, newResult)
                    current.deleteCharAt(current.length - 1) // Remove the last character
                }
                
                if (close < open) {
                    current.append(')')
                    newResult = backtrack(current, pos + 1, open, close + 1, n, newResult)
                    current.deleteCharAt(current.length - 1) // Remove the last character
                }
                newResult
            }
        }
        
        // Initialize the backtracking process
        backtrack(new StringBuilder(), 0, 0, 0, n, List())
    }
}
