use std::collections::HashMap;
use std::cmp::Ordering;

enum HandType {
    FiveOfAKind,
    FourOfAKind,
    FullHouse,
    ThreeOfAKind,
    TwoPair,
    OnePair,
    HighCard,
}

impl PartialOrd for HandType {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        let self_rank = match self {
            HandType::HighCard => 1,
            HandType::OnePair => 2,
            HandType::TwoPair => 3,
            HandType::ThreeOfAKind => 4,
            HandType::FullHouse => 5,
            HandType::FourOfAKind => 6,
            HandType::FiveOfAKind => 7,
        };

        let other_rank = match other {
            HandType::HighCard => 1,
            HandType::OnePair => 2,
            HandType::TwoPair => 3,
            HandType::ThreeOfAKind => 4,
            HandType::FullHouse => 5,
            HandType::FourOfAKind => 6,
            HandType::FiveOfAKind => 7,
        };

        self_rank.partial_cmp(&other_rank)
    }
}   

impl PartialEq for HandType {
    fn eq(&self, other: &Self) -> bool {
        let self_rank = match self {
            HandType::HighCard => 1,
            HandType::OnePair => 2,
            HandType::TwoPair => 3,
            HandType::ThreeOfAKind => 4,
            HandType::FullHouse => 5,
            HandType::FourOfAKind => 6,
            HandType::FiveOfAKind => 7,
        };

        let other_rank = match other {
            HandType::HighCard => 1,
            HandType::OnePair => 2,
            HandType::TwoPair => 3,
            HandType::ThreeOfAKind => 4,
            HandType::FullHouse => 5,
            HandType::FourOfAKind => 6,
            HandType::FiveOfAKind => 7,
        };

        self_rank == other_rank
    }
}

impl Eq for HandType {}

impl Ord for HandType {
    fn cmp(&self, other: &Self) -> Ordering {
        let self_rank = match self {
            HandType::HighCard => 1,
            HandType::OnePair => 2,
            HandType::TwoPair => 3,
            HandType::ThreeOfAKind => 4,
            HandType::FullHouse => 5,
            HandType::FourOfAKind => 6,
            HandType::FiveOfAKind => 7,
        };

        let other_rank = match other {
            HandType::HighCard => 1,
            HandType::OnePair => 2,
            HandType::TwoPair => 3,
            HandType::ThreeOfAKind => 4,
            HandType::FullHouse => 5,
            HandType::FourOfAKind => 6,
            HandType::FiveOfAKind => 7,
        };

        self_rank.cmp(&other_rank)
    }
}
enum CardNumber {
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    Ten,
    Jack, 
    Queen,
    King,
    Ace,
}

impl Ord for CardNumber {
    fn cmp(&self, other: &Self) -> Ordering {
        let self_rank = match self {
            CardNumber::Two => 1,
            CardNumber::Three => 2,
            CardNumber::Four => 3,
            CardNumber::Five => 4,
            CardNumber::Six => 5,
            CardNumber::Seven => 6,
            CardNumber::Eight => 7,
            CardNumber::Nine => 8,
            CardNumber::Ten => 9,
            CardNumber::Jack => 10,
            CardNumber::Queen => 11,
            CardNumber::King => 12,
            CardNumber::Ace => 13,
        };

        let other_rank = match other {
            CardNumber::Two => 1,
            CardNumber::Three => 2,
            CardNumber::Four => 3,
            CardNumber::Five => 4,
            CardNumber::Six => 5,
            CardNumber::Seven => 6,
            CardNumber::Eight => 7,
            CardNumber::Nine => 8,
            CardNumber::Ten => 9,
            CardNumber::Jack => 10,
            CardNumber::Queen => 11,
            CardNumber::King => 12,
            CardNumber::Ace => 13,
        };

        self_rank.cmp(&other_rank)
    }
}

impl PartialOrd for CardNumber {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        let self_rank = match self {
            CardNumber::Two => 1,
            CardNumber::Three => 2,
            CardNumber::Four => 3,
            CardNumber::Five => 4,
            CardNumber::Six => 5,
            CardNumber::Seven => 6,
            CardNumber::Eight => 7,
            CardNumber::Nine => 8,
            CardNumber::Ten => 9,
            CardNumber::Jack => 10,
            CardNumber::Queen => 11,
            CardNumber::King => 12,
            CardNumber::Ace => 13,
        };

        let other_rank = match other {
            CardNumber::Two => 1,
            CardNumber::Three => 2,
            CardNumber::Four => 3,
            CardNumber::Five => 4,
            CardNumber::Six => 5,
            CardNumber::Seven => 6,
            CardNumber::Eight => 7,
            CardNumber::Nine => 8,
            CardNumber::Ten => 9,
            CardNumber::Jack => 10,
            CardNumber::Queen => 11,
            CardNumber::King => 12,
            CardNumber::Ace => 13,
        };

        self_rank.partial_cmp(&other_rank)
    }
}

impl Eq for CardNumber {}

impl PartialEq for CardNumber {
    fn eq(&self, other: &Self) -> bool {
        let self_rank = match self {
            CardNumber::Two => 1,
            CardNumber::Three => 2,
            CardNumber::Four => 3,
            CardNumber::Five => 4,
            CardNumber::Six => 5,
            CardNumber::Seven => 6,
            CardNumber::Eight => 7,
            CardNumber::Nine => 8,
            CardNumber::Ten => 9,
            CardNumber::Jack => 10,
            CardNumber::Queen => 11,
            CardNumber::King => 12,
            CardNumber::Ace => 13,
        };

        let other_rank = match other {
            CardNumber::Two => 1,
            CardNumber::Three => 2,
            CardNumber::Four => 3,
            CardNumber::Five => 4,
            CardNumber::Six => 5,
            CardNumber::Seven => 6,
            CardNumber::Eight => 7,
            CardNumber::Nine => 8,
            CardNumber::Ten => 9,
            CardNumber::Jack => 10,
            CardNumber::Queen => 11,
            CardNumber::King => 12,
            CardNumber::Ace => 13,
        };

        self_rank == other_rank
    }
}

fn convert_card_number(number: &str) -> CardNumber {
    match number {
        "2" => CardNumber::Two,
        "3" => CardNumber::Three,
        "4" => CardNumber::Four,
        "5" => CardNumber::Five,
        "6" => CardNumber::Six,
        "7" => CardNumber::Seven,
        "8" => CardNumber::Eight,
        "9" => CardNumber::Nine,
        "T" => CardNumber::Ten,
        "J" => CardNumber::Jack,
        "Q" => CardNumber::Queen,
        "K" => CardNumber::King,
        "A" => CardNumber::Ace,
        _ => panic!("Invalid card number"),
    }
}



fn compare_hands(hand_1: &str, hand_2: &str) -> Ordering {
    let hand_1_type = get_hand_type(hand_1);
    let hand_2_type = get_hand_type(hand_2);

    if hand_1_type != hand_2_type {
        return hand_1_type.cmp(&hand_2_type);
    }

    let hand_1_cards = hand_1.chars();
    let hand_2_cards = hand_2.chars();

    for (card_1, card_2) in hand_1_cards.zip(hand_2_cards) {
        let card_1 = convert_card_number(&card_1.to_string());
        let card_2 = convert_card_number(&card_2.to_string());

        match card_1.cmp(&card_2) {
            Ordering::Less => return Ordering::Less,
            Ordering::Greater => return Ordering::Greater,
            Ordering::Equal => continue,
        }
    }
    Ordering::Equal
}



fn get_hand_type(cards: &str) -> HandType {

    let cards = cards.chars().collect::<Vec<char>>();
    let mut card_counts = HashMap::new();

    for card in cards {
        let count = card_counts.entry(card).or_insert(0);
        *count += 1;
    }

    let counts = card_counts.values().collect::<Vec<&i32>>();
    if counts.contains(&&5) {
        return HandType::FiveOfAKind;
    }
    if counts.contains(&&4) {
        return HandType::FourOfAKind;
    }
    if counts.contains(&&3) && counts.contains(&&2) {
        return HandType::FullHouse;
    }
    if counts.contains(&&3) {
        return HandType::ThreeOfAKind;
    }
    if counts.contains(&&2) && counts.len() == 3 {
        return HandType::TwoPair;
    }
    if counts.contains(&&2) {
        return HandType::OnePair;
    }
    HandType::HighCard

}
pub fn process_part_1(input: &str) -> i64 {
    // split input into lines
    let lines = input.lines();
    // for each line, split into hand and bid
    let mut hands = lines.map(|line| {
        let mut split = line.split_whitespace();
        let hand = split.next().unwrap();
        let bid = split.next().unwrap();
        (hand, bid)
    }).collect::<Vec<_>>();
    // order hands by type, if type is equal, order by 
    hands.sort_by(|a, b| compare_hands(a.0, b.0));
    
    // hands.reverse();
    hands.iter().enumerate().map(|(index, hand)| {
        let bid = hand.1.parse::<i64>().unwrap();
        let winnings = bid * (index + 1) as i64;
        println!("{} {} {}", hand.0, hand.1, winnings);
        winnings
    }).sum()
    // assign rank based on order
    // multiply rank by bid to calculate winnings
    // sum winnings
}

pub fn process_part_2(input: &str) -> i64 {
    6
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works_1() {
        let input = "32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483";
        let result = process_part_1(input);
        assert_eq!(result, 6440);
    }
//     #[test]
//     fn it_works_2() {
//         let input = "Time:      7  15   30
// Distance:  9  40  200";
//         let result = process_part_2(input);
//         assert_eq!(result, 71503);
//     }

}
