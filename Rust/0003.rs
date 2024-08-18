use std::collections::HashSet;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut seen_chars = HashSet::new();
        let mut start = 0;
        let mut max_length = 0;

        for end in 0..chars.len() {
            while seen_chars.contains(&chars[end]) {
                seen_chars.remove(&chars[start]);
                start += 1;
            }
            seen_chars.insert(chars[end]);
            max_length = max_length.max(end - start + 1);
        }

        max_length as i32
    }
}
