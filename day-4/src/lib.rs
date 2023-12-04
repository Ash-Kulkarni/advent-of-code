pub fn process_part_1(input: &str) -> i32 {

    input
        .lines()
        .map(|card| {
            let parts = &card
                .split(&[':', '|'][..])
                .collect::<Vec<_>>()[1..];

            let card_numbers = parts
                .iter()
                .map(|part| {
                    part
                        .trim()
                        .split_whitespace()
                        .map(|number| number.parse::<i32>().unwrap())
                        .collect::<Vec<_>>()
                })
                .collect::<Vec<_>>();

            let winning_numbers = &card_numbers[0];
            let my_numbers = &card_numbers[1];
            
            let number_of_matches = my_numbers
                .iter()
                .filter(|number| winning_numbers.contains(number))
                .count();

            let score: i32 = match number_of_matches {
                0 => 0 as i32,
                1 => 1 as i32,
                _ => {let mut res = 1; for i in 1..number_of_matches { res *= 2 as i32; } res},
            };

            score
            
        }).sum::<i32>()
    
}



pub fn process_part_2(input: &str) -> i32 {
    
  
    8
}
 
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        let input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11";
        let result = process_part_1(input);
        assert_eq!(result, 13);
    }

    // #[test]
    // fn it_works_2() {
    //     let input = "";
    //     let result = process_part_2(input);
    //     assert_eq!(result, 46);
    // }
}
