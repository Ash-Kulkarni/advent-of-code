pub fn process_part_1(input: &str) -> i32 {

    const MAX_RED: i32 = 12;
    const MAX_GREEN: i32 = 13;
    const MAX_BLUE: i32 = 14;

    input
        .lines()
        .filter_map(|game| {
            let game_input: Vec<_> = game.split(":").collect();
            let game_name = game_input[0];
            let game_id = game_name[5..].parse::<i32>().unwrap();

            let impossible = game_input[1].split(";").map(|hand| {
                let cubes: Vec<_> = hand.split(",").collect();

                for cube in cubes {
                    let cube: &str = cube.trim();
                    let cube_values: Vec<&str> = cube.split(" ").collect();
                    let number = cube_values[0];
                    let colour = cube_values[1];

                    let number = number.parse::<i32>().unwrap();
                    let too_many = match colour {
                        "red" => number > MAX_RED,
                        "green" => number > MAX_GREEN,
                        "blue" => number > MAX_BLUE,
                        _ => panic!("Invalid colour"),
                    };

                    if too_many {
                        return true;
                    }
                
                }
                false
            }).any(|x| x == true);

            if impossible {
                Option::None
            }
            else {
                Option::Some(game_id)
            }
        }).sum()
    
}
pub fn process_part_2(input: &str) -> i32 {
    input
        .lines()
        .map(|game| {
            let mut max_red = 0;
            let mut max_green = 0;
            let mut max_blue = 0;

            let game_input: Vec<_> = game.split(":").collect();

            for hand in game_input[1].split(";") {
                let cubes: Vec<_> = hand.split(",").collect();

                for cube in cubes {
                    let cube: &str = cube.trim();
                    let cube_values: Vec<&str> = cube.split(" ").collect();
                    let number = cube_values[0];
                    let colour = cube_values[1];

                    let number = number.parse::<i32>().unwrap();
                    match colour {
                        "red" => {
                            if number > max_red {
                                max_red = number;
                            }
                        },
                        "green" => {
                            if number > max_green {
                                max_green = number;
                            }
                        },
                        "blue" => {
                            if number > max_blue {
                                max_blue = number;
                            }
                        },
                        _ => panic!("Invalid colour"),
                    };
                }
            }
        max_red * max_green * max_blue
        }).sum()
        }
    


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        let result = process_part_1(input);
        assert_eq!(result, 8);
    }

    #[test]
    fn it_works_2() {
        let input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";
        let result = process_part_2(input);
        assert_eq!(result, 2286);
    }
}
