package main

import (
	"fmt"
)

func main() {
	// learn()
	// learn2()
	// hoe1()
	// hoe2()
	// hoe3()
	// hoe4()
	// hoe5()
	// hoe6()
	// hoe7()
}

// func hoe7() {
// 	var wg sync.WaitGroup
// 	c := make(chan int)

// 	go func() {
// 		for i := 0; i < 10; i++ {
// 			wg.Add(1)
// 			go func(m int) {
// 				for i := 0; i < 10; i++ {
// 					c <- i*10 + m
// 				}
// 				wg.Done()
// 			}(i)
// 		}
// 		wg.Wait()
// 		close(c)
// 	}()

// 	for v := range c {
// 		fmt.Println(v)
// 	}
// }

func hoe6() {
	c := make(chan int)

	go func() {
		for i := 0; i < 10; i++ {
			c <- i
		}
		close(c)
	}()

	for v := range c {
		fmt.Println(v)
	}
}

func hoe5() {
	c := make(chan int)

	go func() {
		c <- 42
	}()
	v, ok := <-c
	fmt.Println(v, ok)

	close(c)

	v, ok = <-c
	fmt.Println(v, ok)
}

func hoe4() {
	q := make(chan int)
	c := gen(q)

	receive(c, q)

	fmt.Println("about to exit")
}

func receive(c, q <-chan int) {
	for {
		select {
		case v := <-c:
			fmt.Println("From c:", v)
		case v := <-q:
			fmt.Printf("All values received (success = %d), returning...\n", v)
			return
		}
	}
}

func gen(q chan<- int) <-chan int {
	c := make(chan int)

	go func() {
		for i := 0; i < 10; i++ {
			c <- i
		}
		q <- 1
		close(c)
	}()

	return c
}

// func hoe3() {
// 	c := gen()
// 	receive(c)

// 	fmt.Println("about to exit")
// }

// func gen() <-chan int {
// 	c := make(chan int)

// 	go func() {
// 		for i := 0; i < 10; i++ {
// 			c <- i
// 		}
// 		close(c)
// 	}()

// 	return c
// }

// func receive(c <-chan int) {
// 	for v := range c {
// 		fmt.Println(v)
// 	}
// }

func hoe2() {
	cs := make(chan int)

	go func() {
		cs <- 42
	}()
	fmt.Println(<-cs)

	fmt.Printf("------\n")
	fmt.Printf("cs\t%T\n", cs)
}

func hoe1() {
	c := make(chan int, 1)

	// Method one, func literal
	// go func() {
	// c <- 42
	// }()

	// Method two, buffer
	c <- 42

	fmt.Println(<-c)
}

// func send(e, o, q chan<- int) {
// 	for i := 0; i < 21; i++ {
// 		if i%2 == 0 {
// 			e <- i
// 		} else {
// 			o <- i
// 		}
// 	}
// 	q <- 0
// }

// func receive(e, o, q <-chan int) {
// 	for {
// 		select {
// 		case v := <-e:
// 			fmt.Println("Even:", v)
// 		case v := <-o:
// 			fmt.Println("\t Odd:", v)
// 		case v := <-q:
// 			fmt.Println("\t\t\tReceived from quit:", v)
// 			return
// 		}
// 	}
// }

// func learn2() {
// 	eve := make(chan int)
// 	odd := make(chan int)
// 	quit := make(chan int)

// 	go send(eve, odd, quit)
// 	receive(eve, odd, quit)

// 	fmt.Println("Exiting...")
// }

// func learn() {
// 	c := make(chan int)
// 	// c <- 42
// 	// fmt.Println(<-c)
// 	// c <- 43
// 	// fmt.Println(<-c)
// 	// fmt.Printf("%T\n", c)

// 	fmt.Println("---")
// 	cr := make(<-chan int)
// 	cs := make(chan<- int)

// 	fmt.Printf("receive: %T\n", cr)
// 	fmt.Printf("send: %T\n", cs)

// 	fmt.Println("----")
// 	go sen(c)
// 	rec(c)
// 	fmt.Println("exit")
// }

// func sen(c chan<- int) {
// 	for i := 0; i < 10; i++ {
// 		c <- i
// 	}
// 	close(c)
// }

// func rec(c <-chan int) {
// 	for v := range c {
// 		fmt.Println(v)
// 	}
// }
