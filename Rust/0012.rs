impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        // Define the values and symbols
        let values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        let symbols = [
            "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ];

        let mut num = num;
        let mut result = String::new();

        // Iterate over the values and symbols
        for (i, &value) in values.iter().enumerate() {
            while num >= value {
                result.push_str(symbols[i]);
                num -= value;
            }
        }

        result
    }
}