package main

import (
	"fmt"
)

var x int = 42
var y string = "James Bond"
var z bool = true

type MyType int

var i MyType
var j int

func main() {
	// hoeOne()
	// hoeTwo()
	// hoeThree()
	// hoeFour()
	hoeFive()
}

func hoeOne() {
	x := 42
	y := "James Bond"
	z := true

	fmt.Printf("%T\n", x)
	fmt.Printf("%T\n", y)
	fmt.Printf("%T\n", z)
	fmt.Println(x, y, z)
}

func hoeTwo() {
	fmt.Printf("%T\n", x)
	fmt.Printf("%T\n", y)
	fmt.Printf("%T\n", z)
	fmt.Println(x, y, z)
}

func hoeThree() {
	s := fmt.Sprintf("Name: %s. Number: %d. Yes? %t", y, x, z)
	fmt.Println(s)
}

func hoeFour() {
	fmt.Println(i)
	fmt.Printf("%T\n", i)
	i = 69
	fmt.Println(i)
}

func hoeFive() {
	hoeFour()
	j = int(i)
	fmt.Println(j)
	fmt.Printf("%T\n", j)
}
