class Solution {

/**
 * @param String $s
 * @param Integer $numRows
 * @return String
 */
function convert($s, $numRows) {
    // Edge case: if numRows is 1 or greater than or equal to the length of s
    if ($numRows == 1 || $numRows >= strlen($s)) {
        return $s;
    }

    // Initialize an array of empty strings for each row
    $rows = array_fill(0, $numRows, '');
    $currentRow = 0;
    $goingDown = false;

    // Traverse each character in the string
    for ($i = 0; $i < strlen($s); $i++) {
        $rows[$currentRow] .= $s[$i];

        // Change direction if we're at the top or bottom row
        if ($currentRow == 0 || $currentRow == $numRows - 1) {
            $goingDown = !$goingDown;
        }

        // Move to the next row
        $currentRow += $goingDown ? 1 : -1;
    }

    // Concatenate all rows to get the final result
    return implode('', $rows);
}
}
