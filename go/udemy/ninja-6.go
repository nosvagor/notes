package main

import (
	"fmt"
	"math"
)

func main() {
	// learn()
	// hoeOne()
	// defer hoeTwo()
	// hoeThree()
	// hoeFour()
	// hoeFive()
	// hoeSix()
	// hoeSeven()
}

func foo() int {
	return 2001
}

func bar() (int, string) {
	return 2001, "Space Odyssey"
}

func hoeOne() {
	i := foo()
	i2, s := bar()
	fmt.Printf("%T\n", i)
	fmt.Println(i)
	fmt.Printf("%T, %T\n", i2, s)
	fmt.Println(i2, s)
}

func foo2(xi ...int) int {
	total := 0
	for _, v := range xi {
		total += v
	}
	return total
}

func bar2(xi []int) int {
	total := 0
	for _, v := range xi {
		total += v
	}
	return total
}

func hoeTwo() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	f2 := foo2(nums...)
	b2 := bar2(append(nums, 11))
	fmt.Println(f2, b2)
}

func hoeThree() {
	defer fmt.Println(foo())
	fmt.Println(bar())
}

type person struct {
	first string
	last  string
	age   int
}

func (p person) speak() {
	fmt.Printf("My name is %s, %s %s, and I am %d years old\n", p.first, p.first, p.last, p.age)
}

func hoeFour() {
	p1 := person{
		first: "Dave",
		last:  "Fuk",
		age:   21,
	}
	p1.speak()
}

type square struct {
	l float64
}

type circle struct {
	r float64
}

func (c circle) area() float64 {
	return math.Pi * math.Pow(c.r, 2)
}

func (s square) area() float64 {
	return math.Pow(s.l, 2)
}

type shape interface {
	area() float64
}

func info(s shape) {
	fmt.Println(s.area())
}

func hoeFive() {
	circ := circle{
		r: 6.28,
	}
	sq := square{
		l: 4,
	}
	info(circ)
	info(sq)
}

func hoeSix() {
	func(s string) {
		fmt.Println("An anonymous function given an", s)
	}("anonymous argument")
}

func hoeSeven() {
	qq := func() {
		for i := 2; i < 10; i++ {
			fmt.Printf("%d tears\n", i)
		}
		fmt.Println("all the tears")
	}
	qq()
}

func returnFunc() func() int {
	return func() int {
		return 42
	}
}

func hoeEight() {
	f := returnFunc()
	fmt.Println(f())
}

// func learn() {
// 	func(x int) {
// 		fmt.Println("Anon func", x)
// 	}(42)

// 	f := func(x int) {
// 		fmt.Println("func expression", 69)
// 	}

// 	f(69)

// 	s1 := foo()
// 	fmt.Println(s1)

// 	x := bar()
// 	fmt.Printf("%T\n", x)
// 	fmt.Println(x())
// 	fmt.Println(bar()())

// 	xi := []int{1, 9, 20, 50, -34, 66, 63, 02, -1, 99}
// 	fmt.Println(sum(xi...))
// 	fmt.Println(even(sum, xi...))

// 	fmt.Println(factorial(5))
// }

// func factorial(n int) int {
// 	if n == 0 {
// 		return 1
// 	}
// 	return n * factorial(n-1)
// }

// func foo() string {
// 	return "Hello world"
// }

// func bar() func() int {
// 	return func() int { return 2001 }
// }

// func sum(xi ...int) int {
// 	total := 0
// 	for _, v := range xi {
// 		total += v
// 	}
// 	return total
// }

// func even(f func(xi ...int) int, vi ...int) int {
// 	yi := []int{}
// 	for _, v := range vi {
// 		if v%2 == 0 {
// 			yi = append(yi, v)
// 		}
// 	}
// 	return f(yi...)
// }
