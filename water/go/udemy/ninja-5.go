package main

import (
	"fmt"
)

type person struct {
	first    string
	last     string
	icecream []string
	age      int
}

func main() {
	// learn()
	// hoeOneToTwo()
	hoeThree()
	// hoeFour()
}

func hoeOneToTwo() {
	p1 := person{
		first:    "Jerry",
		last:     "Smith",
		icecream: []string{"Chocolate", "Vanilla"},
		age:      30,
	}
	p2 := person{
		first:    "Beth",
		last:     "Sanchez",
		icecream: []string{"Mint", "Rocky Road", "Starberry"},
		age:      29,
	}
	fmt.Println(p1)
	fmt.Println(p2)
	for _, v := range p1.icecream {
		fmt.Println(v)
	}

	fmt.Println("-------")

	m := map[string]person{
		p1.last: p1,
		p2.last: p2,
	}

	fmt.Println(m)
	fmt.Println("----------")

	for k, v := range m {
		fmt.Println(k)
		fmt.Println("\t", v.first)
		for i, v := range v.icecream {
			fmt.Println("\t\t", i, v)
		}
	}
}

func hoeThree() {
	type vehicle struct {
		doors int
		color string
	}

	type truck struct {
		vehicle
		fourWheel bool
	}

	cyber := truck{
		vehicle: vehicle{
			doors: 4,
			color: "silver",
		},
		fourWheel: true,
	}

	model3 := struct {
		vehicle
		luxury bool
	}{
		vehicle: vehicle{
			doors: 4,
			color: "white",
		},
		luxury: true,
	}

	fmt.Println(cyber)
	fmt.Println(model3.luxury)
}

func learn() {
	p1 := person{
		first: "James",
		last:  "Bonds",
		age:   32,
	}
	p2 := person{
		first: "Miss",
		last:  "Moneypenny",
		age:   26,
	}

	fmt.Println(p1)
	fmt.Println(p2)
	fmt.Println(p1.first, p1.last)
	fmt.Println(p1.age)

	secretAgent := struct {
		person
		ltk bool
	}{
		person: p1,
		ltk:    true,
	}

	fmt.Println(secretAgent.ltk)
}
