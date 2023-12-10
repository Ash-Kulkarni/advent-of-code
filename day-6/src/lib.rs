pub fn process_part_1(input: &str) -> i64 {
    let data: Vec<Vec<i64>> = input.lines().map(|line| {
        line.split(":").nth(1).unwrap()
            .split_whitespace().map(|n| n.parse::<i64>().unwrap()).collect()
    }).collect();

    let times = &data[0];
    let distances = &data[1];

    times.iter().zip(distances.iter()).map(|(&time, &distance_to_beat)| {
        let possible_distances = get_possible_distances(time);
        possible_distances.iter().filter(|&&d| d>distance_to_beat as i64).count() as i64

    }).product()
}

fn get_possible_distances(time: i64) -> Vec<i64> {
    let mut possible_distances = Vec::new();
    for t in 1..=time {
        possible_distances.push(t*(time-t));
    }
    possible_distances
}

pub fn process_part_2(input: &str) -> i64 {
    let lines: Vec<_> = input.lines().collect();
    let time = lines[0].chars().filter(|c| c.is_digit(10)).collect::<String>().parse::<i64>().unwrap();
    println!("{:?}", time);
    let distance = lines[1].chars().filter(|c| c.is_digit(10)).collect::<String>().parse::<i64>().unwrap();
    
    let possible_distances = get_possible_distances(time);
    possible_distances.iter().filter(|&&d| d > distance as i64).count() as i64 
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        let input = "Time:      7  15   30
Distance:  9  40  200";
        let result = process_part_1(input);
        assert_eq!(result, 288);
    }
    #[test]
    fn it_works_2() {
        let input = "Time:      7  15   30
Distance:  9  40  200";
        let result = process_part_2(input);
        assert_eq!(result, 71503);
    }

}
