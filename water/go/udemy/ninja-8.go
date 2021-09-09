package main

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"os"
	"sort"
	"time"
)

func main() {
	// learn()
	// hoe1()
	// hoe2()
	// hoe3()
	// hoe4()
	hoe5()
}

type User struct {
	First   string
	Last    string
	Age     int
	Sayings []string
}

type ByAge []User
type ByLast []User

func (a ByAge) Len() int           { return len(a) }
func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

func (a ByLast) Len() int           { return len(a) }
func (a ByLast) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByLast) Less(i, j int) bool { return a[i].Last < a[j].Last }

func hoe5() {

	u1 := User{
		First: "James",
		Last:  "Bond",
		Age:   32,
		Sayings: []string{
			"Shaken, not stirred",
			"Youth is no guarantee of innovation",
			"In his majesty's royal service",
		},
	}

	u2 := User{
		First: "Miss",
		Last:  "Moneypenny",
		Age:   27,
		Sayings: []string{
			"James, it is soo good to see you",
			"Would you like me to take care of that for you, James?",
			"I would really prefer to be a secret agent myself.",
		},
	}

	u3 := User{
		First: "M",
		Last:  "Hmmmm",
		Age:   54,
		Sayings: []string{
			"Oh, James. You didn't.",
			"Dear God, what has James done now?",
			"Can someone please tell me where James Bond is?",
		},
	}

	users := []User{u1, u2, u3}
	rand.Seed(time.Now().UnixNano())
	n := rand.Intn(3)
	fmt.Println(n)

	fmt.Println(users)

	fmt.Println("\n---Sorted by Last Name---")
	sort.Sort(ByLast(users))
	for i, v := range users {
		fmt.Printf("Person #%d:\n\t%s %s, Age: %d\n\t\t%s\n", i, v.First, v.Last, v.Age, v.Sayings[n])
	}
	fmt.Println("\n---Sorted by Age---")
	sort.Sort(ByAge(users))
	for i, v := range users {
		fmt.Printf("Person #%d:\n\t%s %s, Age: %d\n\t\t%s\n", i, v.First, v.Last, v.Age, v.Sayings[n])
	}
	fmt.Println(n)
}

func hoe4() {
	xi := []int{5, 8, 2, 43, 17, 987, 14, 12, 21, 1, 4, 2, 3, 93, 13}
	xs := []string{"random", "rainbow", "delights", "in", "torpedo", "summers", "under", "gallantry", "fragmented", "moons", "across", "magenta"}

	fmt.Println(xi)
	// sort.Sort(sort.IntSlice(xi))
	sort.Ints(xi)
	fmt.Println(xi)

	fmt.Println(xs)
	// sort.Sort(sort.StringSlice(xs))
	sort.Strings(xs)
	fmt.Println(xs)
}

func hoe3() {
	type User struct {
		First   string
		Last    string
		Age     int
		Sayings []string
	}

	u1 := User{
		First: "James",
		Last:  "Bond",
		Age:   32,
		Sayings: []string{
			"Shaken, not stirred",
			"Youth is no guarantee of innovation",
			"In his majesty's royal service",
		},
	}

	u2 := User{
		First: "Miss",
		Last:  "Moneypenny",
		Age:   27,
		Sayings: []string{
			"James, it is soo good to see you",
			"Would you like me to take care of that for you, James?",
			"I would really prefer to be a secret agent myself.",
		},
	}

	u3 := User{
		First: "M",
		Last:  "Hmmmm",
		Age:   54,
		Sayings: []string{
			"Oh, James. You didn't.",
			"Dear God, what has James done now?",
			"Can someone please tell me where James Bond is?",
		},
	}

	users := []User{u1, u2, u3}

	// fmt.Println(users)

	err := json.NewEncoder(os.Stdout).Encode(users)
	if err != nil {
		fmt.Println("error:", err)
	}

}

func hoe2() {
	type User struct {
		First   string
		Last    string
		Age     int
		Sayings []string
	}

	s := `[{"First":"James","Last":"Bond","Age":32,"Sayings":["Shaken, not stirred","Youth is no guarantee of innovation","In his majesty's royal service"]},{"First":"Miss","Last":"Moneypenny","Age":27,"Sayings":["James, it is soo good to see you","Would you like me to take care of that for you, James?","I would really prefer to be a secret agent myself."]},{"First":"M","Last":"Hmmmm","Age":54,"Sayings":["Oh, James. You didn't.","Dear God, what has James done now?","Can someone please tell me where James Bond is?"]}]`
	// fmt.Println(s)
	bs := []byte(s)

	var users []User
	err := json.Unmarshal(bs, &users)
	if err != nil {
		fmt.Println("error:", err)
	}
	for i, v := range users {
		fmt.Printf("Person #%d:\n\t%s %s, Age: %d\n\t\t%s\n", i, v.First, v.Last, v.Age, v.Sayings[0])
	}
}

func hoe1() {

	type User struct {
		First string
		Age   int
	}

	u1 := User{
		First: "James",
		Age:   32,
	}

	u2 := User{
		First: "Moneypenny",
		Age:   27,
	}

	u3 := User{
		First: "M",
		Age:   54,
	}

	u4 := User{
		First: "Q",
		Age:   64,
	}

	users := []User{u1, u2, u3, u4}

	fmt.Println(users)

	b, err := json.Marshal(users)
	if err != nil {
		fmt.Println("error:", err)
	}
	os.Stdout.Write(b)
}

// ---------------------------- //

type Person struct {
	Name string
	Age  int
}

func (p Person) String() string {
	return fmt.Sprintf("%s: %d", p.Name, p.Age)
}

// type ByAge []Person

// func (a ByAge) Len() int           { return len(a) }
// func (a ByAge) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
// func (a ByAge) Less(i, j int) bool { return a[i].Age < a[j].Age }

// type ByName []Person

// func (a ByName) Len() int           { return len(a) }
// func (a ByName) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
// func (a ByName) Less(i, j int) bool { return a[i].Name < a[j].Name }

// func learn() {
// 	p1 := Person{"James", 32}
// 	p2 := Person{"Moneypenny", 27}
// 	p3 := Person{"Q", 64}
// 	p4 := Person{"M", 56}

// 	people := []Person{p1, p2, p3, p4}

// 	fmt.Println(people)
// 	sort.Sort(ByAge(people))
// 	fmt.Println(people)
// 	sort.Sort(ByName(people))
// 	fmt.Println(people)
// }
