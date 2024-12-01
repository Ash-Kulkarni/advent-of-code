import gleam/io
import gleam/string
import gleam/list
import gleam/int
import gleam/result
import gleam/pair
import gleam/dict.{type Dict}
import simplifile

const filepath = "input.txt"

fn read_input() -> String {
  let assert Ok(c) = simplifile.read(filepath)
  c |> string.trim
}

fn parse_line(line: String) -> #(Int, Int) {
  let assert [a, b] = line
  |> string.split("   ")
  |> list.map(int.parse)
  |> list.map(result.unwrap(_, 0))
  #(a, b)
}

fn get_diff(input: #(Int, Int)) -> Int {
  let #(a, b) = input
  int.max(a, b) - int.min(a, b)
}

fn reorder(input: List(#(Int, Int))) -> List(#(Int, Int)) {
  let pos0 = input
  |> list.map(pair.first) |> list.sort(int.compare)

  let pos1 = input
  |> list.map(pair.second) |> list.sort(int.compare)

  list.zip(pos0, pos1)

}

fn increment_count_map(map: Dict(Int, Int), key: Int) -> Dict(Int, Int) {
  case dict.get(map, key) {
    Ok(count) -> dict.insert(map, key, count + 1)
    Error(_) -> dict.insert(map, key, 1)
  }
}

fn get_count_map(input: List(Int)) -> Dict(Int, Int) {
  input
  |> list.fold(dict.new(), increment_count_map)
}

fn get_similarity_score(input: Int, count_map: Dict(Int, Int)) -> Int {
  case dict.get(count_map, input) {
    Ok(count) -> count * input
    Error(_) -> 0
  }
}

pub fn main() {

  let data = read_input()
  |> string.split("\n")
  |> list.map(parse_line)

  let _part_1 = data
  |> reorder
  |> list.map(get_diff)
  |> int.sum
  |> io.debug

  let list_2_count_map = data
    |> list.map(pair.second)
    |> get_count_map

  let _part_2 = data
  |> list.map(pair.first)
  |> list.map(get_similarity_score(_, list_2_count_map))
  |> int.sum
  |> io.debug
}
