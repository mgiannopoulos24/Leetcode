public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.Length) {
            return s;
        }
        
        // Initialize a list of strings for each row
        List<string> rows = new List<string>(new string[numRows]);
        for (int i = 0; i < numRows; i++) {
            rows[i] = "";
        }
        
        int currentRow = 0;
        bool goingDown = false;
        
        // Build each row string
        foreach (char c in s) {
            rows[currentRow] += c;
            // Change direction if we're on the first or last row
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }
            // Move to the next row depending on the direction
            currentRow += goingDown ? 1 : -1;
        }
        
        // Concatenate all rows into a single string
        string result = "";
        foreach (string row in rows) {
            result += row;
        }
        
        return result;
    }
}
