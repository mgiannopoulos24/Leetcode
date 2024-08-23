function convert(s: string, numRows: number): string {
    // Edge case: if numRows is 1 or greater than or equal to length of s
    if (numRows === 1 || numRows >= s.length) {
        return s;
    }

    // Initialize an array of empty strings for each row
    const rows: string[] = Array(numRows).fill('');
    let currentRow = 0;
    let goingDown = false;

    // Traverse each character in the string
    for (const char of s) {
        rows[currentRow] += char;

        // Change direction if we're at the top or bottom row
        if (currentRow === 0 || currentRow === numRows - 1) {
            goingDown = !goingDown;
        }

        // Move to the next row
        currentRow += goingDown ? 1 : -1;
    }

    // Concatenate all rows to get the final result
    return rows.join('');
}
