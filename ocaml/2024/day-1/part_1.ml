let read_file filename =
  let channel = open_in filename in
  try
    let length = in_channel_length channel in
    let contents = really_input_string channel length in
    close_in channel;
    contents
  with e ->
    close_in_noerr channel;
    raise e

let process_file_contents contents =
  let lines = String.split_on_char '\n' contents in
  List.iter (Printf.printf "Line: %s\n") lines

let () =
  let filename = "input.txt" in
  try
    let contents = read_file filename in
    process_file_contents contents
  with Sys_error msg -> Printf.eprintf "Error: %s\n" msg
