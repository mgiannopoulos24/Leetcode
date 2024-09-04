class Solution {
    func myAtoi(_ s: String) -> Int {
        // Define the 32-bit signed integer boundaries
        let INT_MIN: Int32 = Int32.min
        let INT_MAX: Int32 = Int32.max

        // Trim leading and trailing whitespace
        var s = s.trimmingCharacters(in: .whitespaces)
        
        // Check for empty string
        if s.isEmpty {
            return 0
        }

        var sign: Int32 = 1
        var result: Int32 = 0
        var index = s.startIndex
        
        // Check for sign
        if s[index] == "-" {
            sign = -1
            index = s.index(after: index)
        } else if s[index] == "+" {
            index = s.index(after: index)
        }

        // Process digits
        while index < s.endIndex, let digit = s[index].wholeNumberValue, let digitValue = Int32(exactly: digit) {
            // Check for overflow before updating the result
            if result > (INT_MAX - digitValue) / 10 {
                return sign == 1 ? Int(INT_MAX) : Int(INT_MIN)
            }
            result = result * 10 + digitValue
            index = s.index(after: index)
        }

        return Int(sign * result)
    }
}