package main

import (
	"fmt"
)

func main() {
	// hoeOne()
	// hoeTwo()
	// hoeThree()
	// hoeFour()
	// hoeFive()
	hoeSix()
}

func hoeOne() {
	for i := 0; i <= 10000; i++ {
		fmt.Println(i)
	}
}

func hoeTwo() {
	for i := 'A'; i < 'Z'+1; i++ {
		for j := 0; j < 3; j++ {
			fmt.Printf("%#U\n", i)
		}
	}
}

func hoeThree() {
	birth := 1996
	for birth <= 2021 {
		fmt.Println(birth)
		birth++
	}
}

func hoeFour() {
	birth := 1996
	for {
		fmt.Println(birth)
		birth++
		if birth > 2021 {
			break
		}
	}
}

func hoeFive() {
	for i := 10; i < 100; i++ {
		fmt.Printf("Number is %d, it's remainder is %d\n", i, i%4)
	}
}

func hoeSix() {
	switch {
	case false:
		fmt.Println("Won't print")
	case true:
		fmt.Println("Will print")
	}
}
