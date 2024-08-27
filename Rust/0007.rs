impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let mut rev = 0;
        let mut num = x;
        
        while num != 0 {
            let pop = num % 10;
            num /= 10;
            
            // Check for overflow/underflow before multiplying rev by 10 and adding pop
            if rev > i32::MAX / 10 || (rev == i32::MAX / 10 && pop > 7) {
                return 0;
            }
            if rev < i32::MIN / 10 || (rev == i32::MIN / 10 && pop < -8) {
                return 0;
            }
            
            rev = rev * 10 + pop;
        }
        
        rev
    }
}
