class Solution {

/**
 * @param String $s
 * @return Integer
 */
function romanToInt($s) {
    // Map to store Roman numeral values
    $romanMap = [
        'I' => 1,
        'V' => 5,
        'X' => 10,
        'L' => 50,
        'C' => 100,
        'D' => 500,
        'M' => 1000
    ];
    
    $total = 0;
    $prevValue = 0;

    // Loop through the string from right to left
    for ($i = strlen($s) - 1; $i >= 0; $i--) {
        $currentChar = $s[$i];
        $currentValue = $romanMap[$currentChar];

        // If the current value is smaller than the previous one, subtract it
        if ($currentValue < $prevValue) {
            $total -= $currentValue;
        } else {
            $total += $currentValue;
        }

        $prevValue = $currentValue;
    }

    return $total;
}
}
