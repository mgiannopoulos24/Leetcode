class Solution {
    func reverse(_ x: Int) -> Int {
        var rev = 0
        var num = x
        
        while num != 0 {
            let pop = num % 10
            num /= 10
            
            // Check for overflow/underflow before updating rev
            if rev > Int32.max / 10 || (rev == Int32.max / 10 && pop > 7) {
                return 0
            }
            if rev < Int32.min / 10 || (rev == Int32.min / 10 && pop < -8) {
                return 0
            }
            
            rev = rev * 10 + pop
        }
        
        return rev
    }
}
