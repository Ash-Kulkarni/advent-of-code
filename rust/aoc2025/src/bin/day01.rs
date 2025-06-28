use std::collections::HashMap;
use std::fs;

fn main() {
    let input = read_input("inputs/day01.txt");
    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

fn read_input(path: &str) -> String {
    fs::read_to_string(path).expect("Failed to read input file")
}

fn part1(input: &str) -> i32 {
    let mut lst1: Vec<i32> = Vec::new();
    let mut lst2: Vec<i32> = Vec::new();
    for line in input.lines() {
        let nums: Vec<i32> = line
            .split_whitespace()
            .filter_map(|x| x.parse().ok())
            .collect();

        if nums.len() != 2 {
            panic!("couldn't find two numbers on line {}", line);
        }

        lst1.push(nums[0]);
        lst2.push(nums[1]);
    }

    lst1.sort();
    lst2.sort();

    lst1.iter().zip(&lst2).map(|(a, b)| (a - b).abs()).sum()
}

fn part2(input: &str) -> i32 {
    let mut lst1: Vec<i32> = Vec::new();
    let mut lst2_count_map: HashMap<i32, i32> = HashMap::new();
    for line in input.lines() {
        let nums: Vec<i32> = line
            .split_whitespace()
            .filter_map(|x| x.parse().ok())
            .collect();

        if nums.len() != 2 {
            panic!("couldn't find two numbers on line {}", line);
        }

        lst1.push(nums[0]);
        *lst2_count_map.entry(nums[1]).or_insert(0) += 1;
    }

    lst1.sort();

    lst1.iter()
        .map(|a| a * lst2_count_map.get(a).unwrap_or(&0))
        .sum()
}
