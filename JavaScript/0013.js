/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    // Map to store Roman numeral values
    const romanMap = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };
    
    let total = 0;
    let prevValue = 0;
    
    // Loop through the string from right to left
    for (let i = s.length - 1; i >= 0; i--) {
        let currentChar = s[i];
        let currentValue = romanMap[currentChar];

        // If the current value is smaller than the previous one, subtract it
        if (currentValue < prevValue) {
            total -= currentValue;
        } else {
            total += currentValue;
        }

        prevValue = currentValue;
    }

    return total;
};
