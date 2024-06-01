package main

import (
	"fmt"
	"sync"
)

var lock = &sync.Mutex{}

type Singleton struct{}

var singleInstance *Singleton

func getInstance() *Singleton {
	/*
		There is a nil-check at the start for making sure singleInstance is empty
		first time around. This is to prevent expensive lock operations every time
		the getinstance method is called. If this check fails, then it means that
		the singleInstance field is already populated.
	*/
	if singleInstance == nil {
		lock.Lock()
		defer lock.Unlock()
		/*
			There is another nil-check after the lock is acquired. This is to ensure
			that if more than one goroutine bypasses the first check, only one
			goroutine can create the singleton instance. Otherwise, all goroutines
			will create their own instances of the singleton struct.
		*/
		if singleInstance == nil {
			fmt.Println("Creating single instance now.")
			singleInstance = &Singleton{}
		} else {
			fmt.Println("Single instance already created.")
		}
	} else {
		fmt.Println("Single instance already created.")
	}

	return singleInstance
}

func main() {
	for i := 0; i < 5; i++ {
		go getInstance()
	}

	fmt.Scanln()
}
