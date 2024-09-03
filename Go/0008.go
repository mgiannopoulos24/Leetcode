package main

import (
	"fmt"
	"math"
	"strings"
	"unicode"
)

func myAtoi(s string) int {
	// Define the 32-bit signed integer boundaries
	const (
		INT_MIN = math.MinInt32
		INT_MAX = math.MaxInt32
	)
	
	// Trim leading whitespaces
	s = strings.TrimLeft(s, " ")
	if len(s) == 0 {
		return 0
	}
	
	// Check for sign
	sign := 1
	if s[0] == '-' {
		sign = -1
		s = s[1:]
	} else if s[0] == '+' {
		s = s[1:]
	}
	
	// Initialize result variable and index
	result := 0
	i := 0
	
	// Process digits
	for i < len(s) && unicode.IsDigit(rune(s[i])) {
		digit := int(s[i] - '0')
		
		// Check for overflow before updating result
		if result > (INT_MAX-digit)/10 {
			if sign == 1 {
				return INT_MAX
			}
			return INT_MIN
		}
		
		result = result*10 + digit
		i++
	}
	
	return sign * result
}
