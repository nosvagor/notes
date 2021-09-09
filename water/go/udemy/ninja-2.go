package main

import "fmt"

const (
	x int = 42
	y     = 69
)

const (
	year = 2021 + iota
	nextYear
	twoYears
	threeYears
	fourYears
)

func main() {
	// hoeOne()
	// hoeTwo()
	// hoeThree()
	// hoeFour(x)
	// hoeFive()
	hoeSix()
}

func hoeOne(n int) {
	fmt.Printf("%d\t%#x\t%b\n", n, n, n)
	fmt.Println("------------")
}

func hoeTwo() {
	g := x == y // false
	h := x <= y // true
	i := x >= y // false
	j := x != y // true
	k := x < y  // true
	l := x > y  // true
	println(g, h, i, j, k, l)
}

func hoeThree() {
	fmt.Printf("%T\t%T\n", x, y)
	fmt.Printf("%d\t%d\n", x, y)
}

func hoeFour(n int) {
	hoeOne(n)
	sx := x << 3
	hoeOne(sx)
}

func hoeFive() {
	s := "\t" + `Raw
	string
	literal`
	fmt.Println(s)
}

func hoeSix() {
	fmt.Println(year, nextYear, twoYears, threeYears, fourYears)
}
