import fs from "fs";
const input = fs.readFileSync("input.txt", "utf8");

const reports = input
  .split("\n")
  .filter((l) => l.trim() !== "")
  .map((x) => x.split(" ").map(Number));

console.log({ reports });
