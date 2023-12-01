
pub fn process_part_1(input: &str) -> i32 {
    input
        .lines()
        .map(|line| {
            let n: String = line
                .chars()
                .filter(|c| c.is_numeric()).collect();

            let first: &str = &n[0..1];
            let last: &str = &n[n.len()-1..n.len()];

            first.to_string() + last
        })
        .map(|s| s.parse::<i32>().unwrap())
        .sum()
        

}

pub fn process_part_2(input: &str) -> i32 {
    const NUMBERS: [&str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    input
        .lines()
        .map(|line| {
            let mut values_found: Vec<String> = Vec::new();

            for (i, c) in line.chars().enumerate() {
                if c.is_numeric() {
                    
                    values_found.push(c.to_string());
                } else {
                    for (j, n) in NUMBERS.iter().enumerate() {
                        if line[i..].starts_with(n) {
                            let num = j+1;
                            let num = num.to_string();
                            values_found.push(num);
                            break;
                        }
                    }
                }
            }

            let n = values_found.join("");
            let first: &str = &n[0..1];
            let last: &str = &n[n.len()-1..n.len()];

            first.to_string() + last
        })
        .map(|s| s.parse::<i32>().unwrap())
        .sum()
        

}
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        let input = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";
        let result = process_part_1(input);
        assert_eq!(result, 142);
    }

    #[test]
    fn it_works_2() {
        let input = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";
        let result = process_part_2(input);
        assert_eq!(result, 281);
    }
}
