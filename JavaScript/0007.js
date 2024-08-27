/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let rev = 0;
    let sign = x < 0 ? -1 : 1;
    x = Math.abs(x);

    while (x !== 0) {
        let pop = x % 10;
        x = Math.floor(x / 10);

        // Check for overflow before updating rev
        if (rev > Math.floor((Math.pow(2, 31) - 1) / 10) ||
            (rev === Math.floor((Math.pow(2, 31) - 1) / 10) && pop > 7)) {
            return 0;
        }
        if (rev < Math.floor(-Math.pow(2, 31) / 10) ||
            (rev === Math.floor(-Math.pow(2, 31) / 10) && pop < -8)) {
            return 0;
        }

        rev = rev * 10 + pop;
    }

    return rev * sign;
};
