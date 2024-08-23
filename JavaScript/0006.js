/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    // Edge cases
    if (numRows === 1 || numRows >= s.length) {
        return s;
    }
    
    // Initialize an array of empty strings for each row
    let rows = new Array(numRows).fill('').map(() => '');
    let currentRow = 0;
    let goingDown = false;
    
    // Traverse each character in the string
    for (let i = 0; i < s.length; i++) {
        rows[currentRow] += s[i];
        
        // Change direction if we're at the top or bottom row
        if (currentRow === 0 || currentRow === numRows - 1) {
            goingDown = !goingDown;
        }
        
        // Move to the next row
        currentRow += goingDown ? 1 : -1;
    }
    
    // Concatenate all rows to get the final result
    return rows.join('');
};
