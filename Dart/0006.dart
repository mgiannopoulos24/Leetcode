class Solution {
  String convert(String s, int numRows) {
    // Edge case: if numRows is 1 or greater than or equal to the length of the string, return the original string
    if (numRows == 1 || numRows >= s.length) {
      return s;
    }
    
    // Initialize a list of strings for each row
    List<StringBuffer> rows = List<StringBuffer>.generate(numRows, (index) => StringBuffer());
    int currentRow = 0;
    bool goingDown = false;

    // Traverse each character in the input string
    for (int i = 0; i < s.length; i++) {
      rows[currentRow].write(s[i]); // Append character to the current row
      
      // Check if we need to change direction (either at the top or bottom row)
      if (currentRow == 0 || currentRow == numRows - 1) {
        goingDown = !goingDown;
      }
      
      // Move to the next row based on the direction
      currentRow += goingDown ? 1 : -1;
    }
    
    // Concatenate all rows to form the final string
    StringBuffer result = StringBuffer();
    for (StringBuffer row in rows) {
      result.write(row.toString());
    }
    
    return result.toString();
  }
}
