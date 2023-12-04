
pub fn process_part_1(input: &str) -> i32 {

    let lines: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();
    let line_count = lines.len();
    let line_length = lines[0].len();

    let mut valid_numbers_sum = 0;

    for (line_number, line) in lines.iter().enumerate() {
        let mut index = 0;
        while index < line_length {
            if line[index].is_digit(10) {
                let mut end_index = index;
                while end_index < line_length && line[end_index].is_digit(10) {
                    end_index += 1;
                }

                if is_valid_sequence(line_length, &lines, line_number, line_count, index, end_index-1) {
                    let number: i32 = line[index..end_index].iter().collect::<String>().parse::<i32>().unwrap();
                    valid_numbers_sum += number;
                }

                index = end_index;
            } else {
                index += 1;
            }
        }
    }

    valid_numbers_sum
}

fn is_valid_sequence(line_length: usize, lines: &[Vec<char>], line_number: usize, line_count: usize, start_index: usize, end_index: usize) -> bool {
    let valid_side = is_valid_side(line_length, &lines[line_number], start_index, end_index);
    let valid_top = line_number > 0 && is_valid_adjacent(line_length, &lines[line_number - 1], start_index, end_index);
    let valid_bottom = line_number < line_count - 1 && is_valid_adjacent(line_length, &lines[line_number + 1], start_index, end_index);


    valid_side || valid_top || valid_bottom
}

fn is_valid_side(line_length: usize, line: &[char], start_index: usize, end_index: usize) -> bool {
    let mut valid = false;
    if start_index > 0 {
        valid = valid || !(line[start_index - 1] == '.' && !line[start_index - 1].is_digit(10));
    }

    if end_index < line_length - 1 {
        valid = valid || !(line[end_index + 1] == '.' && !line[end_index + 1].is_digit(10));
    }

    valid
}

fn is_valid_adjacent(line_length: usize, line: &[char], start_index: usize, end_index: usize) -> bool {

    for i in start_index..=end_index {
        if i < line_length && line[i] != '.' && !line[i].is_digit(10) {
            return true;
        }
    }
    if start_index > 0 && line[start_index - 1] != '.' && !line[start_index - 1].is_digit(10) {
        return true;
    }
    if end_index < line_length - 1 && line[end_index + 1] != '.' && !line[end_index].is_digit(10){
        return true;
    }
    false
}

pub fn process_part_2(input: &str) -> i32 {
    
    let lines: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();
    let line_count = lines.len();
    let line_length = lines[0].len();

    // lines.iter().map(|line| {
    //     line.iter().enumerate()
    //         .filter_map(|(index, c)| c == '*')
    //         .filter_map(|(line, index)| is_gear(line_length, &lines, line, index))
    // }).sum()   
    8
}

fn is_gear(line_length: usize, lines: &[Vec<char>], line: usize, index: usize) -> Result<i32, ()> {
    let mut num_parts = 0;

    // todo

    if num_parts == 2 {
        Ok(get_gear_ratio(line_length, lines, line, index))
    }
    else {
        Err(())
    }

    
}

fn get_gear_ratio(line_length: usize, lines: &[Vec<char>], line: usize, index: usize) -> i32 {
    6
}
    
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        let input = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";
        let result = process_part_1(input);
        assert_eq!(result, 4361);
    }

    #[test]
    fn it_works_2() {
        let input = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";
        let result = process_part_2(input);
        assert_eq!(result, 467835);
    }
}
