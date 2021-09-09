package main

import "fmt"

func main() {
	// learn()
	// hoeOne()
	// hoeTwo()
	// hoeThree()
	// hoeFour()
	// heoFive()
	// hoeSix()
	// hoeSeven()
	hoeEightToTen()
}

func hoeEightToTen() {
	m := map[string][]string{
		`bond_james`: {`Martinis`, `Shaken, not stirred`, `Women`},
		`moneypenny`: {`Literature`, `Computer Science`, `James Bond`},
		`no_dr`:      {`Ice cream`, `Being evil`, `Sunsets`},
	}
	m["fleming_ian"] = []string{`steaks`, `cigars`, `espionage`}
	for k, v := range m {
		fmt.Printf("Type: %T\t Key: %v\n", v, k)
		for _, s := range v {
			fmt.Printf("Type: %T\t Value: %v\n", s, s)
		}
	}
	fmt.Println(`-----hoeTen (delete a key)----`)
	delete(m, `no_dr`)
	for k, v := range m {
		fmt.Printf("Type: %T\t Key: %v\n", v, k)
		for _, s := range v {
			fmt.Printf("Type: %T\t Value: %v\n", s, s)
		}
	}
}

func hoeSeven() {
	x := [][]string{
		{
			"James",
			"Bond",
			`"Shaken, not stirred"`,
		},
		{
			"Miss",
			"Moneypenny",
			`"Helloo, James"`,
		},
	}
	for _, v := range x {
		fmt.Printf("Type: %T\t Value: %v\n", v, v)
		for _, s := range v {
			fmt.Printf("Type: %T\t Value: %v\n", s, s)
		}
	}
}

func hoeSix() {
	x := make([]string, 50)
	fmt.Println(x)
	x = []string{"Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"}
	// with out range clause
	for i := 0; i < len(x); i++ {
		fmt.Printf("Index: %d\t Value: %s\n", i, x[i])
	}
	fmt.Println(cap(x))
	fmt.Println(len(x))
}

func heoFive() {
	x := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	fmt.Println(x)
	x = append(x[:3], x[5:]...)
	fmt.Println(x)
}

func hoeFour() {
	x := []int{42, 43, 44, 45, 46, 47, 48, 49, 50, 51}
	fmt.Println(x)
	x = append(x, 52)
	x = append(x, 53, 54, 55)
	fmt.Println(x)
	y := []int{56, 57, 58, 59, 60}
	x = append(x, y...)
	fmt.Println(x)
}

func hoeThree() {
	x := []int{11, 22, 33, 44, 55, 66, 77, 88, 99, 1010}
	fmt.Println(x[:3])
	fmt.Println(x[6:])
	fmt.Println(x[2:9])
	fmt.Println(x[8:10])
}

func hoeTwo() {
	x := []int{11, 22, 33, 44, 55, 66, 77, 88, 99, 1010}
	for _, v := range x {
		fmt.Println(v)
	}
	fmt.Printf("%T\n", x)
}

func hoeOne() {
	x := [5]int{1, 9, -1, 10, 230}
	for i, v := range x {
		fmt.Println(i, v)
	}
	fmt.Printf("%T\n", x)
}

func learn() {
	// Slice is used instead of array
	x := []int{4, 5, 6, 7, 8, 9}
	fmt.Println(len(x))
	fmt.Println(cap(x))
	fmt.Println(x[0])

	for i, v := range x {
		fmt.Println(i, v)
	}

	fmt.Println("------")

	y := []int{42, 69, 324, 420}
	x = append(x, y...)
	for i, v := range x {
		fmt.Println(i, v)
	}

	fmt.Println("--------")

	x = append(x[:2], x[4:]...)
	for i, v := range x {
		fmt.Println(i, v)
	}

	fmt.Println("--------")

	x = make([]int, 10, 100)
	fmt.Println(x)
	x = append(x[:10], y...)
	fmt.Println(x, len(x), cap(x))

}
