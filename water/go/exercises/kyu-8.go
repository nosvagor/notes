package main

import (
	"fmt"
	"strings"
)

// MakeNegative returns a negative int, even
// if the int was already negative
func MakeNegative(x int) int {
	if x >= 0 {
		return -x
	}
	return x
}

// GetSize returns the surface area and volume
// of a given box in an array [area, volume]
func GetSize(w, h, d int) [2]int {
	area := (2 * (h * w)) + (2 * (h * d)) + (2 * (d * w))
	volume := w * h * d
	return [2]int{area, volume}
}

// IsPalindrome returns a bool value based on whether the
// given string is a palindrome, accounts for non-ASCI strings
func IsPalindrome(str string) bool {
	runes := []rune(strings.ToLower(str))
	length := len(runes)

	for i := 0; i < length/2; i++ {
		if runes[i] != runes[length-1-i] {
			return false
		}
	}
	return true
}

// PositiveSum returns the sum of all positive integers in a slice
func PositiveSum(numbers []int) (sum int) {
	for _, v := range numbers {
		if v > 0 {
			sum += v
		}
	}
	return
}

// TwiceAsOld returns how many years until/ago a father
// will/was twice as old as the child.
func TwiceAsOld(dadYearsOld, sonYearsOld int) int {
	res := dadYearsOld - 2*sonYearsOld
	if res < 0 {
		return -res
	}
	return res
}

// BoolToWord returns "Yes"/"No" instead of true/false
func BoolToWord(word bool) string {
	if word {
		return "Yes"
	}
	return "No"
}

// Summation returns the sum of every number from 1 -> n
func Summation(n int) int {
	return n * (n + 1) / 2
}

func main() {
	fmt.Println(Summation(1))
	fmt.Println(Summation(8))
	fmt.Println(Summation(22))
	fmt.Println(Summation(100))
	fmt.Println(Summation(213))
}
