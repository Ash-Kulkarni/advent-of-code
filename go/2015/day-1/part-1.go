package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("./input.txt")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}

	result := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		for i, c := range line {
			if c == '(' {
				result++
			} else if c == ')' {
				result--
			}
			if result == -1 {
				fmt.Println(i + 1)
				break
			}
		}
		fmt.Println(result)
	}
}
