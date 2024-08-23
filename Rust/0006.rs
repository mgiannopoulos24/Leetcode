impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        // Edge case: if num_rows is 1 or greater than or equal to length of s
        let len = s.len() as i32;
        if num_rows == 1 || num_rows >= len {
            return s;
        }

        // Initialize a vector of empty strings for each row
        let mut rows = vec![String::new(); num_rows as usize];
        let mut current_row = 0;
        let mut going_down = false;

        // Traverse each character in the string
        for char in s.chars() {
            rows[current_row as usize].push(char);

            // Change direction if we're at the top or bottom row
            if current_row == 0 || current_row == num_rows - 1 {
                going_down = !going_down;
            }

            // Move to the next row
            current_row += if going_down { 1 } else { -1 };
        }

        // Concatenate all rows to get the final result
        rows.concat()
    }
}
