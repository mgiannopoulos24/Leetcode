impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let roman_map = vec![
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        ].into_iter().collect::<std::collections::HashMap<_, _>>();
        
        let mut total = 0;
        let mut prev_value = 0;

        // Iterate through the string from right to left
        for ch in s.chars().rev() {
            let current_value = *roman_map.get(&ch).unwrap();

            // If the current value is smaller than the previous one, subtract it
            if current_value < prev_value {
                total -= current_value;
            } else {
                total += current_value;
            }

            prev_value = current_value;
        }

        total
    }
}
