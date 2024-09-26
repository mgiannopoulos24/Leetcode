func romanToInt(s string) int {
    // Map to store Roman numeral values
    romanMap := map[byte]int{
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total := 0
    prevValue := 0

    // Loop through the string from right to left
    for i := len(s) - 1; i >= 0; i-- {
        currentValue := romanMap[s[i]]

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
