impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        // Define the 32-bit signed integer boundaries
        const INT_MIN: i32 = -2_147_483_648;
        const INT_MAX: i32 = 2_147_483_647;

        // Trim leading whitespace
        let s = s.trim();
        if s.is_empty() {
            return 0;
        }

        let mut sign = 1;
        let mut result = 0;
        let mut i = 0;

        // Check for sign
        if let Some(first_char) = s.chars().next() {
            if first_char == '-' {
                sign = -1;
                i += 1;
            } else if first_char == '+' {
                i += 1;
            }
        }

        // Process the digits
        for ch in s[i..].chars() {
            if !ch.is_digit(10) {
                break;
            }
            let digit = ch.to_digit(10).unwrap() as i32;

            // Check for overflow before updating the result
            if result > (INT_MAX - digit) / 10 {
                return if sign == 1 { INT_MAX } else { INT_MIN };
            }

            result = result * 10 + digit;
        }

        sign * result
    }
}
