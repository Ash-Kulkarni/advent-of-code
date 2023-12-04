use day_3::process_part_2;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let result = process_part_2(&input);
    println!("Result: {}", result);
}