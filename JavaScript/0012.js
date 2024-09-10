/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    // Define the values and symbols
    const values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    
    let result = "";

    // Iterate over the values and symbols
    for (let i = 0; i < values.length; i++) {
        // Determine how many times the current value fits into num
        while (num >= values[i]) {
            // Append the corresponding symbol
            result += symbols[i];
            // Reduce num by the value
            num -= values[i];
        }
    }

    return result;
};