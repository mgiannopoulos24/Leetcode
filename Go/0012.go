package main

import "fmt"

func intToRoman(num int) string {
	// Define the symbols and their corresponding values
	vals := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	syms := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}

	result := ""

	// Iterate over each value-symbol pair
	for i := 0; i < len(vals); i++ {
		// Determine how many times the current value fits into num
		count := num / vals[i]
		// Append the symbol count times
		for count > 0 {
			result += syms[i]
			count--
		}
		// Reduce num by the total value added
		num %= vals[i]
	}

	return result
}
