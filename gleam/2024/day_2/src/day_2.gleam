import gleam/io
import gleam/string
import gleam/list
import gleam/int
import gleam/result
import simplifile

const filepath = "input.txt"

fn read_input() -> String {
  let assert Ok(c) = simplifile.read(filepath)
  c |> string.trim
}

fn parse_line(line: String) -> List(Int) {
  line
  |> string.split(" ")
  |> list.map(int.parse)
  |> list.map(result.unwrap(_, 0))
}

fn has_diff_1_to_3(a, b) {
  let v =int.absolute_value(a-b)
  v <= 3 && v >= 1
}


type IncOrDec {
  Inc
  Dec
}


fn all_inc_or_dec_rec(report, inc_or_dec: IncOrDec) {

  case report {
    [_] | [] -> True
    [a, b, ..rest] -> case inc_or_dec {
      Inc -> a<b && all_inc_or_dec_rec([b, ..rest], Inc) && has_diff_1_to_3(a, b)
      Dec -> a>b && all_inc_or_dec_rec([b, ..rest], Dec) && has_diff_1_to_3(a, b)
      
    }
  }

}

fn is_safe(report) {
  case report {
    [_] | [] -> True
    [a, b, ..rest] -> case a < b {
      True -> all_inc_or_dec_rec([b, ..rest], Inc) && has_diff_1_to_3(a, b)
      False -> all_inc_or_dec_rec([b, ..rest], Dec) && has_diff_1_to_3(a, b)
    }
  }

}



fn get_list_without_index(report, index) {
  report
  |> list.index_map(fn(x, i) {#(i, x)})
  |> list.filter(fn(x) {x.0 != index})
  |> list.map(fn(x){x.1})
}

fn get_possible_reports(report: List(v)) -> List(List(v)) {
  report
  |> list.index_map(fn(_x, i) {i})
  |> list.map(fn(i) {get_list_without_index(report, i)})
}


pub fn main() {
  let _part_1 = read_input()
  |> string.split("\n")
  |> list.map(parse_line)
  |> list.filter(is_safe)
  |> list.length
  |> io.debug

  let _part_2 = read_input()
  |> string.split("\n")
  |> list.map(parse_line)
  |> list.map(get_possible_reports)
  |> list.filter(list.any(_, is_safe))
  |> list.length
  |> io.debug
}
