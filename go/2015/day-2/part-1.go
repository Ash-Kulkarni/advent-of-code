package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
  "strconv"
)

func main() {
	file, err := os.Open("./input.txt")
	defer file.Close()
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
  result := 0

	for scanner.Scan() {

		line := scanner.Text()
		parts := strings.Split(line, "x")
    parts_int := []int{}
    for _, p := range parts {
      i, err := strconv.Atoi(p)
      if err != nil {
        log.Fatal(err)
      }
      parts_int = append(parts_int, i)
    }
		l, w, h :=  parts_int[0], parts_int[1], parts_int[2]
		a := l * w
		b := w * h
		c := h * l
    
    volume := l * w * h

    perimeter_1 := 2 * (l + w)
    perimeter_2 := 2 * (l + h)
    perimeter_3 := 2 * (w + h)

    smallest_perimeter := perimeter_1
    if perimeter_2 < smallest_perimeter {
      smallest_perimeter = perimeter_2
    }
    if perimeter_3 < smallest_perimeter {
      smallest_perimeter = perimeter_3
    }

		smallest := a
		if b < smallest {
			smallest = b
		}
		if c < smallest {
			smallest = c
		}
    // result += smallest + 2*l*w + 2*h*l + 2*h*w

    result += smallest_perimeter + volume
	}
  fmt.Println(result)
}
