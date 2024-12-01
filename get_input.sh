#!env/bin/bash

YEAR=$1
DAY=$2
LANG=$3
SESSION=$(cat session.txt)
mkdir -p "$LANG/$YEAR/day_$DAY"
curl -s --cookie "session=$SESSION" https://adventofcode.com/$YEAR/day/$DAY/input > "$LANG/$YEAR/day_$DAY/input.txt"
