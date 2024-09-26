class Solution {
    func romanToInt(_ s: String) -> Int {
        // Dictionary to store Roman numeral values
        let romanMap: [Character: Int] = [
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        ]
        
        var total = 0
        var prevValue = 0
        
        // Loop through the string from right to left
        for char in s.reversed() {
            let currentValue = romanMap[char]!
            
            // If the current value is smaller than the previous one, subtract it
            if currentValue < prevValue {
                total -= currentValue
            } else {
                total += currentValue
            }
            
            prevValue = currentValue
        }
        
        return total
    }
}
