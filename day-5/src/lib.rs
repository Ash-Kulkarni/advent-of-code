use std::collections::HashMap;

pub fn process_part_1(input: &str) -> u32 {

    let parts = input
        .split("\n\n")
        .collect::<Vec<_>>();

    let seeds = parts[0]
        .split_whitespace()
        .skip(1)
        .filter_map(|number| number.parse::<u32>().ok())
        .collect::<Vec<_>>();

    let maps = parts[1..]
        .iter()
        .map(|part| {
            let mut map = HashMap::new();
            part
                .lines()
                .skip(1)
                .map(|line| {
                    line
                        .split_whitespace()
                        .filter_map(|number| number.parse::<u32>().ok())
                        .collect::<Vec<_>>()
                })
                .for_each(|numbers| {
                    let source = numbers[1];
                    let destination = numbers[0];
                    let range = source..source+numbers[2];
                    let diff = source - destination;
                    for s in range {
                        map.insert(s, s - diff);
                    }
                });
            map

        })
        .collect::<Vec<_>>();


    seeds
        .iter()
        .map(|seed| {
            let mut seed = seed.clone();
            for map in &maps {
                seed = *map.get(&seed).unwrap_or(&seed);
            }
            seed
        })
        .min().unwrap()
    
}



pub fn process_part_2(input: &str) -> i32 {
    
  
    8
}
 
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        let input = "seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4";
        let result = process_part_1(input);
        assert_eq!(result, 35);
    }

    // #[test]
    // fn it_works_2() {
    //     let input = "";
    //     let result = process_part_2(input);
    //     assert_eq!(result, 46);
    // }
}
