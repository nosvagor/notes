package main

import (
	"fmt"
	"runtime"
	"sync"
)

func main() {
	// learn()
	learn2()
}

var wg sync.WaitGroup

func foo() {
	for i := 0; i < 5; i++ {
		fmt.Println("foo:", i)
	}
	wg.Done()
}

func bar() {
	for i := 0; i < 5; i++ {
		fmt.Println("bar:", i)
	}
}

func doSomething(x int) int {
	return x * 5
}

func info() {
	fmt.Println("")
	// fmt.Println("OS: \t\t", runtime.GOOS)
	// fmt.Println("ARCH:\t\t", runtime.GOARCH)
	fmt.Println("CPUs:\t\t", runtime.NumCPU())
	fmt.Println("Goroutines:\t", runtime.NumGoroutine())
	fmt.Println("")
}

func learn() {
	wg.Add(1)
	go foo()
	bar()
	info()
	wg.Wait()

	fmt.Println("")

	ch := make(chan int)
	go func() {
		ch <- doSomething(5)
	}()
	fmt.Println(<-ch)
}

func learn2() {
	info()

	counter := 0
	const gs = 42

	wg.Add(gs)

	var mu sync.Mutex

	var r []int

	fmt.Println("Staring loop")

	for i := 0; i < gs; i++ {
		go func() {
			mu.Lock()
			v := counter
			runtime.Gosched()
			v++
			counter = v
			mu.Unlock()
			wg.Done()
		}()
		r = append(r, runtime.NumGoroutine())
	}
	info()
	fmt.Println("Goroutines:", r)
	wg.Wait()

	fmt.Println("")
	fmt.Println("Counter:", counter)

}
