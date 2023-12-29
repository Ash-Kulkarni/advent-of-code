use day_9::process_part_1;
use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    let result = process_part_1(&input);
    println!("Result: {}", result);
}
