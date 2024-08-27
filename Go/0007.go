package main

import (
	"fmt"
	"math"
	"strconv"
)

func reverse(x int) int {
	// Define the 32-bit signed integer range
	const (
		minInt = math.MinInt32
		maxInt = math.MaxInt32
	)

	// Handle the sign
	negative := x < 0
	if negative {
		x = -x
	}

	// Convert the absolute value to a string
	strX := strconv.Itoa(x)
	reversedStr := reverseString(strX)

	// Convert the reversed string back to an integer
	reversedInt, err := strconv.Atoi(reversedStr)
	if err != nil {
		return 0
	}

	// Apply the original sign to the reversed integer
	if negative {
		reversedInt = -reversedInt
	}

	// Check for overflow
	if reversedInt < minInt || reversedInt > maxInt {
		return 0
	}

	return reversedInt
}

// Helper function to reverse a string
func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}